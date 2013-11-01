from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInLine(admin.TabularInline):
    model = Choice
    #extra = 3  #extra is 3 by default

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Poll Info', {'fields': ['question', 'total_votes']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]
    
    #Changes the display on the "change list page"
    list_display = ('question', 'total_votes', 'pub_date', 'was_published_recently')   #column headings for each entry
    list_filter = ['pub_date']      #adds filter window on right
    search_fields = ['question']    #adds a search box
    #date_hierarchy = 'pub_date'

#class ChoiceAdmin(admin.ModelAdmin):
#    fields = ['poll', 'choice_text']

admin.site.register(Poll, PollAdmin)

#admin.site.register(Choice)#, ChoiceAdmin)