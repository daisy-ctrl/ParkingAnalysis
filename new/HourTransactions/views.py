from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from analysis.models import All

def hourTransactions(request):
    return render(request, 'hourTransactions.html')

def hourTransactions_chart(request):
    labels = []
    data = []

    queryset = All.objects.values('Hour').annotate(amount=Sum('amount')).order_by('-amount')
    for entry in queryset:
        labels.append(entry['Hour'])
        data.append(entry['amount'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
