import datetime

from django.shortcuts import render
from django.utils import timezone

from .models import Record


# Create your views here.
def start(request):
    current_record = Record.objects.create()

    return render(request, 'zerf/start.html', {'record': current_record})


def stop(request):
    current_record = Record.objects.filter(
        start_time__lte=timezone.now()).order_by('-start_time')[0]

    if current_record.stop_time == None:
        current_record.stop_time = timezone.now()
        current_record.interval = current_record.stop_time - current_record.start_time
        current_record.save()

        return render(request, 'zerf/stop.html', {'record': current_record})
    else:
        return render(request, 'zerf/error.html')


def list_all(request):
    summe = datetime.timedelta()

    records = Record.objects.all().order_by('-start_time')

    for record in records:
        summe += record.interval

    return render(request, 'zerf/list_all.html',
        {
            'records': records,
            'summe': summe
        })
