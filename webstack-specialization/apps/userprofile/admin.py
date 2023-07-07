from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from .models import Profile

admin.site.register(Profile)