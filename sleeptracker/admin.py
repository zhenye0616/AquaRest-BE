# sleeptracker/admin.py
from django.contrib import admin
from .models import SleepRecord

class SleepRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'sleep_time_hours', 'sleepiness_level')  # Fields to display in list view
    search_fields = ['date']  # Fields to search in admin list view
    list_filter = ('date', 'sleepiness_level')  # Filters to use in admin list view

# Register the admin class with the associated model
admin.site.register(SleepRecord, SleepRecordAdmin)