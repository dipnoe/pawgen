from django.contrib import admin

from order.models import Order, Application


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'amount',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'owner', 'specie', 'breed', 'sex', 'birth_date', 'extra_information', 'create_date',)
    list_filter = ('owner', 'specie', 'sex', )
