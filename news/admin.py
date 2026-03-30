from django.contrib import admin
from .models import Category, Newsletter, Subscriber

# Register models so they show in admin
admin.site.register(Category)
admin.site.register(Newsletter)
admin.site.register(Subscriber)
