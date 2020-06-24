from django.db import models


# Created Table with Columns
class ItemTb(models.Model):
    itemNameCol = models.CharField(max_length=100)
    itemDecCol = models.CharField(max_length=300)
    itemTextCol = models.CharField(max_length=2000)
    itemImageCol = models.CharField(max_length=300)
    itemPriceCol = models.IntegerField()
    itemSellCol = models.IntegerField()