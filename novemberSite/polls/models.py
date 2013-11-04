import datetime
from django.utils import timezone
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    total_votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.question
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)    #each Choice is related to Poll
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0);  #models.FloatField(default=0)
    
    def __unicode__(self):
        return self.choice_text
    
    def setPercentage(self, total_votes):
        if(total_votes != 0):
            self.percentage = round(float(self.votes*100) / total_votes) # len(poll.choice_set.all()))
            self.save()
        else:
            self.percentage = 0;