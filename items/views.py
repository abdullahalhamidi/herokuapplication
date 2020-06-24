from django.shortcuts import render
import json
import urllib.request
from . import models, admin
from django.http import HttpResponse
from .models import ItemTb


def items(request):
    if not models.ItemTb.objects.all():
        # Download raw json objects
        item_url = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/item.json"
        item_data = urllib.request.urlopen(item_url).read().decode()

        # Parse json object
        item_obj = json.loads(item_data)
        # Access json elements

        for item in item_obj['data']:
            itemName = item_obj['data'][item]['name']
            itemDec = item_obj['data'][item]['description']
            itemText = item_obj['data'][item]['plaintext']
            itemImage = item_obj['data'][item]['image']['full']
            itemPrice = item_obj['data'][item]['gold']['base']
            itemSell = item_obj['data'][item]['gold']['sell']
            # Insert into item table
            itemssavedata = models.ItemTb()
            itemssavedata.itemNameCol = itemName
            itemssavedata.itemDecCol = itemDec
            itemssavedata.itemTextCol = itemText
            itemssavedata.itemImageCol = itemImage
            itemssavedata.itemPriceCol = itemPrice
            itemssavedata.itemSellCol = itemSell
            itemssavedata.save()
    else:
        # ItemTb.objects.all().delete()
        print("There is data in the database")

    itemsdata = ItemTb.objects.all()
    itemname = request.GET.get('search')
    if itemname != '' and itemname is not None:
        itemsdata = itemsdata.filter(itemNameCol=itemname)
    return render(request, 'items.html', {'itemsdata': itemsdata})
