import os
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-secret-key')
DEBUG = False
ALLOWED_HOSTS = ['travelguidewebsite.onrender.com', '127.0.0.1', 'localhost']

# Applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base',
    'authentication',

    'cloudinary',
    'cloudinary_storage',
]

# Cloudinary configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('dq72kr1f2'),
    'API_KEY': os.getenv('615182765469458'),
    'API_SECRET': os.getenv('bF_xUba8zqk3TD5zjOdzMD8_yZM'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs and templates
ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # dev static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')    # collected static for prod
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Messages
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Default primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
