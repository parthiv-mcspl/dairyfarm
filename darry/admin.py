from django.contrib import admin
from .models import Info
from .models import Product
from .models import Book
from.models import Review

admin.site.register(Info)
admin.site.register(Product)
admin.site.register(Book)
admin.site.register(Review)