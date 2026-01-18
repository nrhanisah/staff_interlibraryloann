import os
from django.core.wsgi import get_wsgi_application

# Pastikan nama ini 'staff_interlibraryloan.settings' ikut nama folder anda
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()