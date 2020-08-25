from django.urls import path

from busiest_subcounty_by_weekday import views

urlpatterns = [
    path('', views.subcounty_weekday, name='subcounty_weekday'),
    path('weekday-chart/', views.weekday_chart, name='weekday-chart'),
]
