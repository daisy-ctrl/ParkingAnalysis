# Create your views here.
from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from analysis.models import All

def Hour(request):
    return render(request, 'hour.html')

def hour_chart(request):
    labels = []
    data = []

    queryset = All.objects.values('Hour').annotate(id=Count('id')).order_by('-id')
    for entry in queryset:
        labels.append(entry['Hour'])
        data.append(entry['id'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
