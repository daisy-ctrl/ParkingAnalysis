from django.urls import path

from daily_traffic_count import views

urlpatterns = [
    path('', views.weekday, name='weekday'),
    path('weekday-chart/', views.weekday_chart, name='weekday-chart'),
]
