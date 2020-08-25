from django.urls import path

from Hour import views

urlpatterns = [
    path('', views.Hour, name='hour'),
    path('hour-chart/', views.hour_chart, name='hour'),
]
