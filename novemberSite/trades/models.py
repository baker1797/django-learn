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
    
    
    
    
#class StatLine(models.Model):
#    minutes = models.FloatField(default=0)
#    fgm = models.FloatField(default=0)
#    fga = models.FloatField(default=0)
#    fgp = models.FloatField(default=0)
#    ftm = models.FloatField(default=0)
#    fta = models.FloatField(default=0)
#    ftp = models.FloatField(default=0)
#    threes = models.FloatField(default=0)
#    rebounds = models.FloatField(default=0)
#    assists = models.FloatField(default=0)
#    steals = models.FloatField(default=0)
#    blocks = models.FloatField(default=0)
#    points = models.FloatField(default=0)


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
    position = models.CharField(max_length=10)
    
    #stat_line = models.OneToOneField(StatLine)
    
    minutes = models.FloatField(default=0)
    fgm = models.FloatField(default=0)
    fga = models.FloatField(default=0)
    fgp = models.FloatField(default=0)
    ftm = models.FloatField(default=0)
    fta = models.FloatField(default=0)
    ftp = models.FloatField(default=0)
    threes = models.FloatField(default=0)
    rebounds = models.FloatField(default=0)
    assists = models.FloatField(default=0)
    steals = models.FloatField(default=0)
    blocks = models.FloatField(default=0)
    points = models.FloatField(default=0)
    
    def __unicode__(self):
        return self.name
    
    def update_stats(self, stat_line):
        self.minutes = stat_line[0]
        
        fg = (stat_line[1]).split('/')
        self.fgm = fg[0]
        self.fga = fg[1]
        self.fgp = stat_line[2]
        
        ft = (stat_line[3]).split('/')
        self.ftm = ft[0]
        self.fta = ft[1]
        self.ftp = stat_line[4]
        
        self.threes = stat_line[5]
        self.rebounds = stat_line[6]
        self.assists = stat_line[7]
        self.steals = stat_line[8]
        self.blocks = stat_line[9]
        self.points = stat_line[10]
        self.save()
    
    
    
    
    
    
    
    
    
    
    
    
    