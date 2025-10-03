# 🌳 TreeHub - Django Tree Information Portal

A comprehensive Django-based web application dedicated to tree education, forest conservation awareness, and practical tree care guidance. TreeHub serves as an educational platform providing valuable resources about tree species, forest ecosystems, and environmental stewardship.

## 🌟 Features

- **🏠 Home Page** - Welcome interface with featured trees and comprehensive site overview
- **ℹ️ About Section** - Mission statement, values, and TreeHub's commitment to environmental conservation
- **🌲 Tree Types** - Detailed guide covering tree categories and identification (Deciduous, Evergreen, Fruit Trees, Flowering Trees)
- **🌍 Forest Facts** - Educational content about forest ecosystems, biodiversity, and environmental impact
- **🌱 Tree Care** - Comprehensive guidance for tree planting, maintenance, pruning, and seasonal care
- **📱 Responsive Design** - Mobile-first design that works seamlessly across all devices
- **🎨 Nature-Inspired UI** - Clean, minimal interface with earth-tone colors and intuitive navigation
- **🐳 Docker Ready** - Complete containerization for easy deployment and development
- **⚡ Static Content** - No database dependencies for simplicity

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ (recommended: Python 3.11+)
- pip (Python package installer)
- virtualenv (recommended for isolated environment)
- Git (for version control)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/iamchandrashekhar/treehub.git
   cd treehub
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Linux/macOS:
   source .venv/bin/activate
   
   # On Windows:
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables (optional)**
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Visit the application**
   Open your browser and navigate to: `http://127.0.0.1:8000`

### Verify Installation

After starting the server, you should see:
- Home page with tree information and navigation
- All 5 main sections accessible through the navigation menu
- Responsive design working on different screen sizes

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root for environment-specific settings:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Static Files
STATIC_ROOT=/var/www/treehub/static/

# Security Settings (for production)
SECURE_BROWSER_XSS_FILTER=True
SECURE_CONTENT_TYPE_NOSNIFF=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### Production Settings

For production deployment, make sure to:

1. **Set DEBUG to False**
2. **Use a strong SECRET_KEY**
3. **Configure ALLOWED_HOSTS**
4. **Configure static file serving**
5. **Ensure SQLite database is properly backed up**

## 🐳 Docker Deployment

TreeHub includes complete Docker support for both development and production environments.

### Development with Docker

1. **Start development environment**
   ```bash
   docker-compose -f docker-compose.dev.yml up --build
   ```

2. **Run in background**
   ```bash
   docker-compose -f docker-compose.dev.yml up -d
   ```

3. **View logs**
   ```bash
   docker-compose -f docker-compose.dev.yml logs -f
   ```

4. **Stop services**
   ```bash
   docker-compose -f docker-compose.dev.yml down
   ```

### Production with Docker

1. **Build and run production environment**
   ```bash
   docker-compose up --build -d
   ```

2. **Access the application**
   - Application: `http://localhost:80`
   - Nginx handles static files and reverse proxy

3. **View production logs**
   ```bash
   docker-compose logs -f
   ```

4. **Stop production services**
   ```bash
   docker-compose down
   ```

### Manual Docker Commands

1. **Build development image**
   ```bash
   docker build -t treehub:dev .
   ```

2. **Build production image**
   ```bash
   docker build -f Dockerfile.prod -t treehub:prod .
   ```

3. **Run container manually**
   ```bash
   docker run -p 8000:8000 treehub:dev
   ```

## 🏭 Production Deployment

### Using Gunicorn

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Run with Gunicorn**
   ```bash
   gunicorn treehub.wsgi:application --bind 0.0.0.0:8000
   ```

### Using Docker in Production

1. **Build production image**
   ```bash
   docker build -f Dockerfile.prod -t treehub:prod .
   ```

2. **Run with environment variables**
   ```bash
   docker run -d \
     -p 80:8000 \
     -e DEBUG=False \
     -e SECRET_KEY=your-production-secret-key \
     -e ALLOWED_HOSTS=yourdomain.com \
     treehub:prod
   ```

### Development Tools

```bash
# Check for code issues
python manage.py check

# Validate templates
python manage.py check --deploy

# Collect static files
python manage.py collectstatic

# Start development server with specific settings
python manage.py runserver --settings=treehub.settings
```

### Environment Configuration Examples

**Development (.env)**
```env
SECRET_KEY=django-insecure-your-dev-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

**Production (.env)**
```env
SECRET_KEY=your-strong-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
STATIC_ROOT=/var/www/treehub/static/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Why Trees Matter
Trees are essential for:
- 🌍 **Climate regulation** - absorbing CO2 and producing oxygen
- 🏠 **Wildlife habitats** - supporting biodiversity
- 🌊 **Water cycle** - preventing erosion and filtering water
- 💚 **Human well-being** - providing shade, beauty, and peace


---

**Happy Tree Planting! 🌱**