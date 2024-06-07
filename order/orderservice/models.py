from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='orderservices/',max_length=250,null=True,default=None)

    def __str__(self):
        return self.name

class OrderList(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)


    def __str__(self):
        total_price = self.quantity * self.menu_item.price
        return f'{self.quantity} x {self.menu_item.name} for {self.customer.first_name} - Total: {total_price}'
    
    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.menu_item.price
        super().save(*args, **kwargs)









