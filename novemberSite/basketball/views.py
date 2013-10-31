from django.shortcuts import render

#from basketball.models import Team, Player
from basketball.models import Team, Player


def index(request):
    context = {
        'teams': Team.objects.order_by('city'),
        'players': Player.objects.all()
    }
    return render(request, 'basketball/index.html', context)

def player_card(request, player_id):
    context = {
        'player': Player.objects.get(id=player_id)
    }
    return render(request, 'basketball/player_card.html', context)
