from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from analysis.models import All

def home(request):
        return render(request, 'home.html')

def subcounty_chart(request):
    labels = []
    data = []

    queryset = All.objects.values('Sub_name').annotate(id=Count('id')).order_by('-id')
    for entry in queryset:
        labels.append(entry['Sub_name'])
        data.append(entry['id'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
