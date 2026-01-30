# NerdyDoodler's Art Portfolio Website

A professional Python Flask-based artist portfolio website inspired by tommyarnoldart.com. This website showcases artwork, provides contact functionality, and includes client information - perfect for artists, illustrators, and concept designers.

http://portfolio.eba-prxmsc4t.us-east-1.elasticbeanstalk.com/

## Features

- **Portfolio Gallery**: Categorized artwork display with concept art and illustrations
- **Responsive Design**: Mobile-friendly layout using Tailwind CSS
- **Contact Form**: Functional contact form with message storage
- **Mailing List**: Email subscription functionality
- **Client Showcase**: Display of entertainment and publishing clients
- **About Section**: Professional artist biography and services
- **Dynamic Content**: Database-driven artwork and client management
- **Modal Views**: Interactive artwork detail modals

## Technology Stack

- **Backend**: Python 3.8+, Flask, SQLAlchemy
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL)
- **Forms**: Flask-WTF with validation
- **Icons**: Font Awesome

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd artist-portfolio
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## Project Structure

```
artist-portfolio/
├── app.py                 # Main Flask application
├── init_db.py            # Database initialization script
├── requirements.txt      # Python dependencies
├── templates/           # HTML templates
│   ├── base.html       # Base template with navigation
│   ├── index.html      # Homepage with featured work
│   ├── work.html       # Portfolio gallery with filters
│   ├── gallery.html    # Category-specific galleries
│   ├── about.html      # About page and client showcase
│   └── contact.html    # Contact form and information
├── static/             # Static assets (CSS, JS, images)
│   └── uploads/        # User uploaded images
└── portfolio.db        # SQLite database (created automatically)
```

## Configuration

### Database Configuration

The default configuration uses SQLite. To use a different database, modify `app.py`:

```python
# PostgreSQL example
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/portfolio'

# MySQL example
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/portfolio'
```

### Secret Key

Change the secret key in `app.py` for production:

```python
app.config['SECRET_KEY'] = 'your-secure-secret-key-here'
```

## Adding Content

### Adding Artwork

You can add artwork through the database:

```python
from app import app, db, Artwork

with app.app_context():
    artwork = Artwork(
        title="Artwork Title",
        category="concept-art",  # or "illustration"
        description="Description of the artwork",
        image_url="path/to/image.jpg",
        client="Client Name",
        year=2024,
        featured=True  # Set to True for homepage display
    )
    db.session.add(artwork)
    db.session.commit()
```

### Adding Clients

```python
from app import app, db, Client

with app.app_context():
    client = Client(
        name="Client Name",
        category="Entertainment",  # or "Publishing"
        logo_url="path/to/logo.jpg",
        website_url="https://client-website.com"
    )
    db.session.add(client)
    db.session.commit()
```

## Customization

### Styling

The website uses Tailwind CSS. You can customize colors and styles by modifying the CSS classes in the templates. The primary color is purple (`#667eea`).

### Images

Place your artwork images in the `static/uploads/` directory and reference them accordingly in the database.

### Contact Information

Update contact details in `templates/contact.html` to reflect your actual contact information.

## Deployment

### Heroku

1. Install Heroku CLI and login
2. Create a `Procfile`:
   ```
   web: python app.py
   ```
3. Deploy:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python", "app.py"]
```

## Features Breakdown

### Homepage
- Hero section with artist introduction
- Featured artwork gallery
- Iconic projects showcase
- Call-to-action section
- Mailing list signup

### Portfolio Pages
- Filterable artwork gallery
- Category-specific views (Concept Art, Illustration)
- Interactive modal views for artwork details
- Responsive grid layout

### About Page
- Artist biography
- Services overview
- Industries served
- Client logos and information

### Contact Page
- Functional contact form with validation
- Contact information display
- Social media links
- FAQ section
- Mailing list signup

## Security Considerations

- CSRF protection enabled via Flask-WTF
- Input validation on all forms
- SQL injection protection via SQLAlchemy ORM
- Secure secret key configuration needed for production

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or support, please open an issue in the repository or contact the developer.

---

**Note**: This is a template website. Replace placeholder content, images, and contact information with your own to create your professional artist portfolio.
