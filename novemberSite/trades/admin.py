from django.contrib import admin

from trades.models import Team, Player #, StandingsStats, StatLine

class PlayerInLine(admin.TabularInline):
    model = Player
    #extra = 3  #extra is 3 by default
#    
#class StatLineInLine(admin.TabularInline):
#    model = StatLine
#    #extra = 3  #extra is 3 by default

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team', {'fields': ['name', 'current_points']}),
        #('Roster', {'fields': ['pub_date']})
    ]
    inlines = [PlayerInLine]
    
    list_display = ('name', 'current_points')
    
class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic', {'fields': ['name', 'team'],}),
        #('Roster', {'fields': ['pub_date']})
    ]
    #inlines = [StatLineInLine]
    
    #list_display = ('name', 'current_points')
    
# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Player)#, PlayerAdmin)
#admin.site.register(StatLine)