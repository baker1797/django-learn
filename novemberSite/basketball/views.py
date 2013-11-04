from django.shortcuts import render

from polls.models import Poll

from basketball.models import Team, Player
def index(request):
    context = {
        'teams': Team.objects.order_by('city'),
        'players': Player.objects.all(),
        'poll': Poll.objects.get(id=1),
    }
    return render(request, 'basketball/index.html', context)

def player_card(request, player_id):
    context = {
        'player': Player.objects.get(id=player_id)
    }
    return render(request, 'basketball/player_card.html', context)

#@register.inclusion_tag('show_menu_teams.html')
#def show_menu_teams():
#    teams = Team.objects.order_by('city')
#    return { 'teams': teams }