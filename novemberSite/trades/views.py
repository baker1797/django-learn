from django.shortcuts import render

from trades.models import Team, Player

def index(request):
    context = {
        'teams': Team.objects.all(),
    }
    return render(request, 'trades/index.html', context)

def team(request, team_id):
    context = {
        'teams': Team.objects.get(id=team_id),
        'players': Team.player_set.all(),
    }
    return render(request, 'trades/team.html', context)
