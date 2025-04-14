# Fashion Store E-commerce Website

A modern e-commerce website built with Django for selling fashion products.

## Features

- Product catalog with categories
- Shopping cart functionality
- Product search
- Responsive design
- Admin panel for managing products and categories

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd fashionstore
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
MEDIA_URL=/media/
MEDIA_ROOT=media
STATIC_URL=/static/
STATIC_ROOT=staticfiles
```

5. Apply migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Access the website at http://127.0.0.1:8000/

## Environment Variables

- `DEBUG`: Set to False in production
- `SECRET_KEY`: Django secret key (keep this secret!)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection URL
- `MEDIA_URL`: URL prefix for media files
- `MEDIA_ROOT`: Path to media files directory
- `STATIC_URL`: URL prefix for static files
- `STATIC_ROOT`: Path to static files directory

## Security Notes

- Never commit the `.env` file to version control
- Change the `SECRET_KEY` in production
- Set `DEBUG=False` in production
- Use a proper database in production (not SQLite)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Bootstrap Icons 