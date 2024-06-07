from django.contrib import admin
from orderservice.models import MenuItem,OrderList
class Menu(admin.ModelAdmin):
    list_display=('name','description','price','image')
    
    
admin.site.register(MenuItem,Menu)

admin.site.register(OrderList)

    

# Register your models here.
