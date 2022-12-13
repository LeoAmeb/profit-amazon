from django.db import models

# Create your models here.
class Order(models.Model):
    ASIN = models.CharField(max_length=10)
    SKU = models.CharField(max_length=10)
    AmazonOrderItemCode = models.CharField(max_length=15)
    NumberOfItems = models.IntegerField()
    ProductName= models.CharField(max_length=200)
    Quantity= models.IntegerField()
    ItemStatus= models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.ASIN