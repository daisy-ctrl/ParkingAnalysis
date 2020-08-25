"""new URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('analysis/',include('analysis.urls')),
    path('busiest_subcounty/',include('busiest_subcounty.urls')),
    path('busiest_subcounty_by_weekday/',include('busiest_subcounty_by_weekday.urls')),
    path('daily_traffic_count/',include('daily_traffic_count.urls')),
    path('average_daily_transactions/',include('average_daily_transactions.urls')),
    path('Hour/',include('Hour.urls')),
    path('HourTransactions/',include('HourTransactions.urls')),
    path('admin/', admin.site.urls),

]
