# Logement - Real Estate Management Platform

A modern Django web application for managing residential properties, enabling seamless communication between tenants and property owners.

## Overview

Logement is a comprehensive real estate management platform built with Django and a modern responsive UI. The platform facilitates apartment listings, user communication, and administrative oversight of property listings.

## Key Features

- **Apartment Listings**: Property owners can create, modify, and manage apartment listings with multiple images
- **Dual-User System**: Support for tenants (locataires) and property owners (propriétaires)
- **Real-Time Messaging**: Direct communication between tenants and property owners within the platform
- **Favorites Management**: Tenants can save and manage favorite apartments
- **Content Moderation**: Admin dashboard for reviewing and approving listings
- **Report System**: Users can report inappropriate listings with admin review workflow
- **Responsive Design**: Modern mobile-first UI with dark mode support

## Technology Stack

- **Backend**: Django 6.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development)
- **UI Framework**: Custom CSS with Manrope & Playfair Display fonts
- **Architecture**: MVC pattern with form-based interactions

## Project Structure

```
.
├── appartement/          # Apartments app - listings and details
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── message/              # Messaging app - conversations
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── user/                 # User management - auth and profiles
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── favoris/              # Favorites app - saved apartments
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── logement/             # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── template/             # HTML templates
├── static/               # CSS and JavaScript assets
├── manage.py
└── requirements.txt
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup Steps

```bash
# Clone repository
git clone https://github.com/yourusername/logement.git
cd logement

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit `http://localhost:8000/` to access the application.

## User Roles

### Tenant (Locataire)
- Browse available apartments
- Save favorites
- Contact property owners
- View conversation history
- Manage profile

### Property Owner (Propriétaire)
- Create and manage apartment listings
- Upload multiple property images
- View and respond to tenant inquiries
- Monitor listing status
- Check conversation messages

### Admin
- Approve/reject pending listings
- Review user reports
- Manage users
- Monitor platform activity
- Resolve disputes

## Core Models

### User
Custom user model with role-based access (TENANT, OWNER, ADMIN)

### Appartement
Stores apartment details: title, description, location, price, availability status, moderation status

### AppartementImage
Multiple images per apartment with safe URL handling

### Conversation
Manages messaging between tenants and owners linked to specific apartments

### Message
Individual messages with timestamps and sender information

### Favoris
User's saved apartment preferences

### Signalement (Report)
User reports for inappropriate listings with admin workflow

## API Endpoints

### Apartments
- `GET /app/` - Homepage (public)
- `GET /app/feed/` - Apartment listings (authenticated)
- `GET /app/appartement/<id>/` - Apartment details
- `POST /app/ajouter/` - Create listing (owner only)
- `POST /app/appartement/<id>/modifier/` - Edit listing
- `POST /app/appartement/<id>/supprimer/` - Delete listing

### Messaging
- `GET /mes/conversations/` - All conversations
- `GET /mes/conversation/<id>/` - Specific conversation
- `POST /mes/conversation/<id>/` - Post message
- `GET /mes/conversations/nouveau/<logement_id>/` - Start conversation

### User
- `GET /account/login/` - Login page
- `POST /account/login/` - Login handler
- `GET /account/register/` - Registration
- `POST /account/register/` - Register handler
- `GET /account/profil/` - User profile

### Favorites
- `GET /fav/mes-favoris/` - User's favorites

## Development Guidelines

### Code Style
- Follow PEP 8 for Python
- Use descriptive variable and function names
- Add docstrings to all views and models
- Keep views focused and DRY

### Database
- Use Django ORM for all database operations
- Implement `select_related()` and `prefetch_related()` for query optimization
- Use transaction management for multi-step operations

### Testing
Run tests with:
```bash
python manage.py test
```

## Security Notes

- User authentication required for sensitive operations
- Permission checks on all data modifications
- CSRF protection on all POST forms
- SQL injection prevention via ORM
- XSS protection via template escaping

## Future Enhancements

- Payment integration for rental bookings
- Advanced search filters and map integration
- Notification system
- Review/rating system
- Automated property recommendation
- API for mobile apps

## Contributing

1. Create feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -m "Add feature description"`
3. Push to branch: `git push origin feature/your-feature`
4. Open pull request

## License

This project is proprietary. All rights reserved.

## Support

For issues and questions, please open an issue on the GitHub repository.

---

**Version**: 1.0.0  
**Last Updated**: April 23, 2026
