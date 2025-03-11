from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    description=models.TextField()
    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        return self.stock>0

    def reduce_stock(self,quantity):
        if self.stock<quantity:
            return False
        self.stock-=quantity
        self.save()

        class Meta:
            ordering=["name"]
