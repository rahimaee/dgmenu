# 🍽️ Smart Restaurant & Cafe Menu Management System (DGMenu)

## 📋 Project Overview

**DGMenu** is a comprehensive smart menu management system for cafes and restaurants that enables managers to fully manage menus, cafe information, and customer interactions. The system includes an administrative panel for the main administrator and personal panels for each cafe/restaurant.

## ✨ Key Features

### 🏢 Main Administrator Panel
- Management of all cafes and restaurants
- System performance monitoring
- User and role management
- Comprehensive reporting

### 🏪 Cafe/Restaurant Manager Panel
- Food menu and category management
- Image upload and gallery management
- Team information management
- Cafe customization settings
- Table and reservation management

### 👥 User Panel
- View cafe menus
- Search and filter foods
- View cafe and team information
- Image gallery

## 🛠️ Technologies Used

### Backend
- **Django 3.2.5** - Main web framework
- **Python 3.x** - Programming language
- **SQLite** - Database (can be changed to PostgreSQL/MySQL)

### Frontend
- **HTML5/CSS3** - Structure and styling
- **JavaScript** - User interaction
- **Bootstrap** - CSS framework (likely)

### Django Libraries
- **django-crispy-forms** - Beautiful forms
- **django-filter** - Data filtering
- **django-mptt** - Tree structure
- **django-taggit** - Tagging system
- **djangorestframework** - REST API
- **Pillow** - Image processing
- **social-auth-app-django** - Social authentication

### Security
- **cryptography** - Encryption
- **PyJWT** - JWT tokens
- **defusedxml** - XML security

## 📁 Project Structure

```
dgmenu/
├── dgmenu/                    # Main Django settings
├── adminpanel/               # Main admin panel
├── dgmenu_cafe/             # Cafe models
├── dgmenu_food/             # Food management
├── dgmenu_food_category/    # Food categories
├── dgmenu_cafe_team/        # Cafe team management
├── dgmenu_cafe_gallery/     # Image gallery
├── dgmenu_cafe_about/       # About page
├── dgmenu_cafe_tabel/       # Table management
├── dgmenu_cafe_viewers/     # Cafe viewer
├── dgmenu_account/          # Account management
├── dgmenu_account_role/     # User roles
├── dgmenu_site_home/        # Site homepage
├── templates/               # HTML templates
├── static_cdn/              # Static files
└── assets/                  # Additional resources
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip
- virtualenv (recommended)

### Installation Steps

1. **Clone the project**
```bash
git clone [repository-url]
cd dgmenu
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Run development server**
```bash
python manage.py runserver
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Database Configuration
For PostgreSQL usage:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dgmenu_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📊 Data Models

### Cafe
- Complete cafe information (name, address, contact)
- Logo and various icons
- Page background images
- SEO settings and social media

### Food & Category
- Food management with images
- Multi-level categories
- Pricing and descriptions

### Team & Gallery
- Team member management
- Cafe image gallery

### Tables
- Table and reservation management

## 🔐 Authentication System

- Multi-level authentication (main admin, cafe manager, user)
- Role and permission system
- Social authentication (Instagram, Facebook)

## 🎨 Customization

Each cafe can:
- Upload their own logo and icons
- Change page colors and styles
- Customize background images
- Manage contact information and social media

## 📱 Mobile Features

- Responsive design
- Mobile device optimization
- Various icons for iOS and Android

## 🔍 SEO & Optimization

- Configurable meta tags
- Optimized URL structure
- XML sitemap
- robots.txt file

## 📈 Reporting

- Visit statistics
- Sales reports
- Cafe performance analysis

## 🚀 Deployment

### For Production
```bash
# Set DEBUG = False
# Set ALLOWED_HOSTS
# Collect static files
python manage.py collectstatic

# Use WSGI server
gunicorn dgmenu.wsgi:application
```

### Passenger Support
The `passenger_wsgi.py` file is ready for deployment on Passenger servers.

## 🤝 Contributing

1. Fork the project
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the [MIT](LICENSE) License.

## 📞 Support

For questions and support:
- Email: [your-email@domain.com]
- Phone: [your-phone-number]
- Website: [hamyarmenu.ir](https://hamyarmenu.ir)

## 🔄 Versions

- **Current Version**: 1.0.0
- **Last Update**: [Date]

---

**Developer**: [Your Name]
**Created**: [Date] 