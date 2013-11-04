from django.db import models

#import micromodels
#
#class StandingsStats(micromodels.Model):
#    fgp = micromodels.IntegerField(default=0)
#    ftp = micromodels.IntegerField(default=0)
#    threes = micromodels.IntegerField(default=0)
#    rebounds = micromodels.IntegerField(default=0)
#    assists = micromodels.IntegerField(default=0)
#    steals = micromodels.IntegerField(default=0)
#    blocks = micromodels.IntegerField(default=0)
#    points = micromodels.IntegerField(default=0)
#    
#    def __unicode__(self):
#        return "StandingsStats"
#
#class StatLine(StandingsStats):
#    minutes = micromodels.IntegerField(default=0)
#    fgm = micromodels.IntegerField(default=0)
#    fga = micromodels.IntegerField(default=0)
#    ftm = micromodels.IntegerField(default=0)
#    fta = micromodels.IntegerField(default=0)
#    
#    def __unicode__(self):
#        return "StatLine"
    
class Team(models.Model):
    name = models.CharField(max_length=30)
    current_points = models.IntegerField(default=0)
    current_standings = {} #micromodels.ModelCollectionField(StatLine)
    total_stats = {} #micromodels.ModelCollectionField(StatLine)
    
    def __unicode__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=40)
    team = models.ForeignKey(Team)
    #position = models.CharField(max_length=10)
    #stat_line = micromodels.ModelCollectionField(StatLine)
    
    minutes = models.IntegerField(default=0)
    fgm = models.IntegerField(default=0)
    fga = models.IntegerField(default=0)
    fgp = models.IntegerField(default=0)
    ftm = models.IntegerField(default=0)
    fta = models.IntegerField(default=0)
    ftp = models.IntegerField(default=0)
    threes = models.IntegerField(default=0)
    rebounds = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    steals = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
    
    