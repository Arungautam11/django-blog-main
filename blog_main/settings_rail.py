from blog_main.settings import *

from decouple import config

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = ['django-blog-main-production.up.railway.app']