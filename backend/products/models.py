from django.db import models
from django.conf import settings
from decimal import Decimal

#3.53---->Associating a user to a model 
user=settings.AUTH_USER_MODEL 
# Create your models here.
class Product (models.Model):
    #You cna find the pk of each 
    user=models.ForeignKey(user,default=1,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(decimal_places=2,max_digits=15,default=99.99)

    @property
    def sale_price(self):

        return "%.2f" %(float(self.price) * 0.8)
        #return self.price*float('0.8')
    
    def get_discount(self):
         return (Decimal(float(122))-self.price)