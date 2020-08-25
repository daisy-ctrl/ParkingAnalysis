from django.urls import path

from HourTransactions import views

urlpatterns = [
    path('', views.hourTransactions, name='hour'),
    path('hourTransactions-chart/', views.hourTransactions_chart, name='hourTransactions-chart'),
]
