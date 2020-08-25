# Create your views here.
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from analysis.models import All

def transactions(request):
    return render(request, 'transactions.html')

def transactions_chart(request):
    labels = []
    data = []

    queryset = All.objects.values('Sub_name').annotate(amount=Sum('amount')).order_by('-amount')
    for entry in queryset:
        labels.append(entry['Sub_name'])
        data.append(entry['amount'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
