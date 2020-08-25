# Create your models here.
from django.db import models

class All(models.Model):
	id = models.IntegerField(primary_key=True)
	sale_id = models.CharField(max_length=20)
	amount = models.IntegerField()
	Hour = models.IntegerField()
	Weekday_Name = models.CharField(max_length=10)
	Sub_name = models.CharField(max_length=20)
	subcounty_id = models.IntegerField()

class average_daily_transactions(models.Model):
	amount = models.IntegerField()
	Weekday_Name = models.CharField(max_length=10)
	Sub_name = models.CharField(max_length=20)

class busiest_subcounty_by_weekday(models.Model):
	id = models.IntegerField(primary_key=True)
	Weekday_Name = models.CharField(max_length=10)
	Sub_name = models.CharField(max_length=20)

class busiest_subcounty(models.Model):
	id = models.IntegerField(primary_key=True)
	Sub_name = models.CharField(max_length=20)

class daily_traffic_count(models.Model):
	id = models.IntegerField(primary_key=True)
	Weekday_Name = models.CharField(max_length=10)
	Sub_name = models.CharField(max_length=20)

class busiest_hour(models.Model):
	id = models.IntegerField(primary_key=True)
	Hour = models.IntegerField()
	Sub_name = models.CharField(max_length=20)
