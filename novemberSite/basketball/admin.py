from django.contrib import admin
from basketball.models import Team, Player  #, Stats


class PlayerInLine(admin.TabularInline):
    model = Player
    #extra = 3  #extra is 3 by default

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Team', {'fields': ['city', 'name']}),
        #('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [PlayerInLine]
    
    list_display = ('name', 'city')
    
# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Player)