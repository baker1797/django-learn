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
    "Display the team and roster to trade with"
    #t = get_object_or_404(Team, pk=request.POST['team'])
    
    try:
        t = get_object_or_404(Team, pk=request.POST['team'])
        #t = Team.objects.all(pk=request.POST['team'])
    except(KeyError, Team.DoesNotExist):
        return render(request, 'trades/index.html', {
            'error_message': "You didn't select a team",
        })
    else:
        stat_fields = ("Name", "Pos.", "Min.", "FGM", "FGA", "FG%", \
                       "FTM", "FTA", "FT%", "3's", "Reb", "Assists", "Steals", "Blocks", "Pts")
        
        return render(request, 'trades/tradeEnviro.html', {'team': t, 'stat_fields': stat_fields})

def editPlayer(request, team_id):
    "Edit a player's stat fields after submission"
    
    #Get the POST variables
    try:
        player = get_object_or_404(Player, pk=request.POST['player_id'])
        stat_line = (request.POST['stats_update']).split('\t')
        team = get_object_or_404(Team, pk=team_id)
        
    except(KeyError, Player.DoesNotExist):
        return render(request, 'trades/index.html', {
            'error_message': "You didn't select a team",
        })
    else:
        #Update player's stats
        if(len(stat_line) != 11):
            pass
        else:
            player.update_stats(stat_line)
            
            
            #player.minutes = stat_line[0]
            #
            #fg = (stat_line[1]).split('/')
            #player.fgm = fg[0]
            #player.fga = fg[1]
            #player.fgp = stat_line[2]
            #
            #ft = (stat_line[3]).split('/')
            #player.ftm = ft[0]
            #player.fta = ft[1]
            #player.ftp = stat_line[4]
            #
            #player.threes = stat_line[5]
            #player.rebounds = stat_line[6]
            #player.assists = stat_line[7]
            #player.steals = stat_line[8]
            #player.blocks = stat_line[9]
            #player.points = stat_line[10]
            #
            player.save()
            
        context = {
            'team': team,
            'player': player,
        }
    
    #return render(request, 'trades/team.html', {'team': team, 'roster': roster,})
    return render(request, 'trades/index.html', context)


    #return render(request, 'trades/editPlayer.html', {'player': player, 'stat_fields': stat_fields})
    