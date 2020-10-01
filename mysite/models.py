from django.db import models

class ShopData(models.Model):
    item_id=models.CharField(max_length=40)
    item_name=models.CharField(max_length=100)
    item_category=models.CharField(max_length=100)
    sub_cat=models.CharField(max_length=100)
    stock=models.IntegerField()
    price=models.IntegerField(null=True)

    class Meta:
        db_table='Data'
    def __str__(self):
        return self.item_name
class cart(models.Model):
    item=models.ForeignKey(ShopData,on_delete=models.CASCADE)
    qty=models.IntegerField()
    pid=models.CharField(max_length=100)
    add_on=models.DateTimeField(auto_now=True)
    price=models.IntegerField()

    def __str__(self):
        return str(self.item)
class bill(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=12)
    final=models.IntegerField()
    date_time=models.DateTimeField(auto_now_add=True,blank=False,editable=True)
    items=models.TextField()
    address=models.TextField()
    status=models.CharField(max_length=20)
    bill_number=models.CharField(max_length=200)

    def __str__(self):
        return self.name

