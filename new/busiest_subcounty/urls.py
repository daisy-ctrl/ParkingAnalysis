from django.urls import path
from busiest_subcounty import views

urlpatterns = [
    path('subcounty-chart/', views.subcounty_chart, name='subcounty-chart'),
    path('', views.home, name='home'),
]
