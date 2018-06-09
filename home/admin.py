from django.contrib import admin

# Register your models here.
from .models import Driver, About

admin.site.register(Driver)
admin.site.register(About)
