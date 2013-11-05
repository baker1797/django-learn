from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from trades.models import Team, Player

def index(request):
    "View a list of the teams and select a team to trade with"
    context = {
        'teams': Team.objects.all(),
    }
    return render(request, 'trades/index.html', context)

def team(request, team_id):
    "View a team and its roster"
    team = get_object_or_404(Team, pk=team_id)
    roster = team.player_set.all()
    
    return render(request, 'trades/team.html', {'team': team, 'roster': roster,})

def tradeEnviro(request):
    "Handle the vote submission after a user completes a poll"
    #t = get_object_or_404(Team, pk=request.POST['team'])
    
    try:
        t = get_object_or_404(Team, pk=request.POST['team'])
        #t = Team.objects.all(pk=request.POST['team'])
    except(KeyError, Team.DoesNotExist):
        return render(request, 'trades/index.html', {
            'error_message': "You didn't select a team",
        })
    else:
        stat_fields = ("Name", "Min.", "FGM", "FGA", "FG%", \
                       "FTM", "FTA", "FT%", "3's", "Reb", "Assists", "Steals", "Pts")
        
        return render(request, 'trades/tradeEnviro.html', {'team': t, 'stat_fields': stat_fields})
    
#def editPlayer(request, player_id):
def editPlayer(request):
    "Edit a player's stat fields after submission"
    
    player = get_object_or_404(Player, pk=request.POST['player_id'])
    player.minutes = request.POST['stats_update']
    context = {}
    
    #return render(request, 'trades/team.html', {'team': team, 'roster': roster,})
    return render(request, 'trades/index.html', context)


    #return render(request, 'trades/editPlayer.html', {'player': player, 'stat_fields': stat_fields})

    
    
    
##########################
##########################

    #t = get_object_or_404(Team, pk=request.POST['team'])
    #try:
    #    t = t.player_set.get(pk=request.POST['team'])
    #except(KeyError, Choice.DoesNotExist):
    #    return render(request, 'polls/detail.html', {
    #        'poll': p,
    #        'error_message': "You didn't select a choice",
    #    })
    #else:
    #    selected_choice.votes += 1
    #    selected_choice.save()
    #    p.total_votes += 1
    #    p.save()
    #    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    
    
    #context = {
    #    'teams': selected_team, #Team.objects.get(id=team_id),
    ##    'players': Team.player_set.all(),
    #}
    #
    ##return HttpResponseRedirect(reverse('trades:index', args=(t.id,)))
    #return render(request, 'trades/team.html', context)
    