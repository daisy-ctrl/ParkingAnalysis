from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from analysis.models import All

# Create your views here.
def weekday(request):
    return render(request, 'weekday.html')

def weekday_chart(request):
    labels = []
    data = []

    queryset = All.objects.values('Weekday_Name').annotate(id=Count('id')).order_by('-id')
    for entry in queryset:
        labels.append(entry['Weekday_Name'])
        data.append(entry['id'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
