from django.urls import path

from average_daily_transactions import views

urlpatterns = [
     path('', views.transactions, name='transactions'),
     path('transactions-chart/', views.transactions_chart, name='transactions_chart'),
]
