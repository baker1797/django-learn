from django.db import models


class Team(models.Model):
    name = models.CharField(max_length = 20)
    city = models.CharField(max_length = 30)
    roster_size = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.name
    
    #def adjust_roster_size(self, ):
    #    pass
    
    
class Player(models.Model):
    team = models.ForeignKey(Team)  #defined by p.player_set.create()
    
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    #jersey = models.IntegerField()
    
    def __unicode__(self):
        return self.last_name + ", " + self.first_name

#class Stats(models.Model):
#    threes = models.IntegerField(default = 0)
#    rebounds = models.IntegerField(default = 0)
#    assists = models.IntegerField(default = 0)
#    steals = models.IntegerField(default = 0)
#    blocks = models.IntegerField(default = 0)
#    points = models.IntegerField(default = 0)
#    
#    def __unicode__(self):
#        return self.player
