# sleeptracker/forms.py
from django import forms
from .models import SleepRecord

class SleepRecordForm(forms.ModelForm):
    class Meta:
        model = SleepRecord
        fields = ['date', 'sleep_time_hours', 'sleepiness_level']
