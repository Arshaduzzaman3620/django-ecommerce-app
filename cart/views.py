from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from shop.models import Product
from .models import Cart, CartItem
from django.contrib import messages

def get_cart(request):
    cart_id = request.session.get('cart_id')
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    return cart

def cart_detail(request):
    try:
        cart = get_cart(request)
        context = {
            'cart': cart,
            'title': 'Your Shopping Cart'
        }
        return render(request, 'cart/detail.html', context)
    except Exception as e:
        messages.error(request, f'Error loading cart: {str(e)}')
        return redirect('shop:product_list')

@require_POST
def cart_add(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        cart = get_cart(request)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': 1}
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product.name} added to cart successfully!',
                'cart_total': cart.get_total_price()
            })
        
        messages.success(request, f'{product.name} added to cart successfully!')
        return redirect('cart:cart_detail')
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': f'Error adding product to cart: {str(e)}'
            }, status=500)
        messages.error(request, f'Error adding product to cart: {str(e)}')
        return redirect('shop:product_list')

@require_POST
def cart_update(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        cart = get_cart(request)
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        
        data = json.loads(request.body)
        quantity = data.get('quantity', 1)
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        
        return JsonResponse({
            'success': True,
            'message': f'{product.name} quantity updated successfully!',
            'cart_total': cart.get_total_price()
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Error updating cart: {str(e)}'
        }, status=500)

@require_POST
def cart_remove(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
        cart = get_cart(request)
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)
        cart_item.delete()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'{product.name} removed from cart successfully!',
                'cart_total': cart.get_total_price()
            })
        
        messages.success(request, f'{product.name} removed from cart successfully!')
        return redirect('cart:cart_detail')
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'message': f'Error removing product from cart: {str(e)}'
            }, status=500)
        messages.error(request, f'Error removing product from cart: {str(e)}')
        return redirect('cart:cart_detail')
