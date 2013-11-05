from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from trades.models import Team, Player

def index(request):
    context = {
        'teams': Team.objects.all(),
    }
    return render(request, 'trades/index.html', context)

def tradeEnviro(request):
    "Handle the vote submission after a user completes a poll"
    #t = get_object_or_404(Team, pk=request.POST['team'])
    
    try:
        t = get_object_or_404(Team, pk=request.POST['team'])
        #t = Team.objects.all(pk=request.POST['team'])
        #t = t.player_set.get(pk=request.POST['team'])
    except(KeyError, Team.DoesNotExist):
        return render(request, 'trades/index.html', {
            'team': t,
            'error_message': "You didn't select a team",
        })
    else:
        #context = {
        #    'teams': selected_team, #Team.objects.get(id=team_id),
        ##    'players': Team.player_set.all(),
        #}
        #
        ##return HttpResponseRedirect(reverse('trades:index', args=(t.id,)))
        #return render(request, 'trades/team.html', context)
        return render(request, 'trades/tradeEnviro.html', {'team': t,})
    
   

def team(request, team_id):
    "Handle the vote submission after a user completes a poll"
    #t = get_object_or_404(Team, pk=team_id)
    t = get_object_or_404(Team, pk=request.POST['team'])
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
    return render(request, 'trades/team.html', {'team': t,})
    
    
    
    #context = {
    #    'teams': selected_team, #Team.objects.get(id=team_id),
    ##    'players': Team.player_set.all(),
    #}
    #
    ##return HttpResponseRedirect(reverse('trades:index', args=(t.id,)))
    #return render(request, 'trades/team.html', context)
    
    
#def results(request, poll_id):
#    "Display the poll's results after processing the data"
#    poll = get_object_or_404(Poll, pk=poll_id)
#    
#    for choice in poll.choice_set.all():
#        choice.setPercentage(poll.total_votes)
#
#    return render(request, 'polls/results.html', {'poll': poll, 'total_votes': poll.total_votes})
