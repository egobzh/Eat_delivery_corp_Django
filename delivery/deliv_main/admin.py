from django.contrib import admin
from .models import Worker,Food,Order,Food_order

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display=('name',)
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display=('name','price')
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('date','order_worker')
@admin.register(Food_order)
class Foood_orderAdmin(admin.ModelAdmin):
    list_display=('orderr',)