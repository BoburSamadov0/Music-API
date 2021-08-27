from django.contrib import admin
from .models import Song, Album, Artist

admin.site.register([Song, Album, Artist])
