from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Record(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    stop_time = models.DateTimeField(blank=True, null=True)
    interval = models.DurationField(default=timedelta(minutes=1))
