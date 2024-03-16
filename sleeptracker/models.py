from django.db import models

class SleepRecord(models.Model):
    date = models.DateField()
    sleep_time_hours = models.DecimalField(max_digits=4, decimal_places=2)
    sleepiness_level = models.IntegerField()

    def __str__(self):
        return f"Record for {self.date}: {self.sleep_time_hours} hours, Level {self.sleepiness_level}"