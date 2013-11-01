from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'
    
    def get_queryset(self):
        """Return the last five published polls"""
        return Poll.objects.order_by('-pub_date')[:5]

def anotherPage(request):
    return HttpResponse("Hello, world. You're at more.")

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    
#def detail(request, poll_id):
#    poll = get_object_or_404(Poll, pk=poll_id)
#    return render(request, 'polls/detail.html', {'poll': poll})
#

def results(request, poll_id):
    "Display the poll's results after processing the data"
    poll = get_object_or_404(Poll, pk=poll_id)
    
    for choice in poll.choice_set.all():
        choice.setPercentage(poll.total_votes)

    return render(request, 'polls/results.html', {'poll': poll, 'total_votes': poll.total_votes})

def vote(request, poll_id):
    "Handle the vote submission after a user completes a poll"
    p = get_object_or_404(Poll, pk=poll_id)
    
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        p.total_votes += 1
        p.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))