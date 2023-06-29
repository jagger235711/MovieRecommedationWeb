from django.contrib import admin

import userWeb
from .models import Movie, Profile

# Register your models here.
admin.site.register(Movie)
admin.site.register(Profile)
