from django.contrib import admin
from .models import Product, Image

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'date', 'price', 'photo')
	search_fields = ('name', 'date', 'price')
	list_editable = ('price', 'description')

admin.site.register(Product)
admin.site.register(Image)
