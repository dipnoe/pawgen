from django.contrib import admin

from main.models import Category, Service


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'is_available', 'category', )
    list_filter = ('category',)
