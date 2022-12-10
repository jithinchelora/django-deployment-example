from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category_name
    
    
class ItemDetails(models.Model):
    name = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()
    availability = models.BooleanField(default=False)
    
    category = models.ForeignKey(Category,related_name='item',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name




    