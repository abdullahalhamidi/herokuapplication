from django.shortcuts import render
import json
import urllib.request
from . import models, admin
from django.http import HttpResponse
from .models import ChampionsTb


def champions(request):
    if not models.ChampionsTb.objects.all():
        # Download raw json object
        url = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json"
        data = urllib.request.urlopen(url).read().decode()

        # Parse json object
        obj = json.loads(data)

        # Access json elements
        for id in obj['data']:
            idname = obj['data'][id]['id']
            name = obj['data'][id]['name']
            # title = obj['data'][id]['title']
            blurb = obj['data'][id]['blurb']
            # attack = obj['data'][id]['info']['attack']
            # defense = obj['data'][id]['info']['defense']
            # magic = obj['data'][id]['info']['magic']
            difficulty = obj['data'][id]['info']['difficulty']
            # image = obj['data'][id]['image']['full']
            hp = obj['data'][id]['stats']['hp']
            # movespeed = obj['data'][id]['stats']['movespeed']
            # armor = obj['data'][id]['stats']['armor']
            # attackrange = obj['data'][id]['stats']['attackrange']
            # hpregen = obj['data'][id]['stats']['hpregen']
            attackdamage = obj['data'][id]['stats']['attackdamage']
            # attackspeed = obj['data'][id]['stats']['attackspeed']
            # Insert into table
            championssavedata = models.ChampionsTb()
            championssavedata.idCol = idname
            championssavedata.nameCol = name
            # championssavedata.titleCol = title
            championssavedata.blurbCol = blurb
            # championssavedata.attackCol = attack
            # championssavedata.defenseCol = defense
            # championssavedata.magicCol = magic
            championssavedata.difficultyCol = difficulty
            # championssavedata.imageCol = image
            championssavedata.hpCol = hp
            # championssavedata.movespeedCol = movespeed
            # championssavedata.armorCol = armor
            # championssavedata.attackrangeCol = attackrange
            # championssavedata.hpregenCol = hpregen
            championssavedata.attackdamageCol = attackdamage
            # championssavedata.attackspeedCol = attackspeed
            championssavedata.save()
    else:
        # ChampionsTb.objects.all().delete()
        print("There is data in the database")

    championsdata = ChampionsTb.objects.all()
    champname = request.GET.get('search')
    if champname != '' and champname is not None:
        championsdata = championsdata.filter(idCol=champname)
    print(champname)
    return render(request, 'champions.html', {'championsdata': championsdata})
