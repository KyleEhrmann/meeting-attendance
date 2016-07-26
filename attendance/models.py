from django.db import models
from django.utils import timezone


# Create your models here.
class Person(models.Model):

	name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=12)
	email_address = models.CharField(max_length=255)
	date_of_meeting = models.DateField(default=timezone.now)
	attended = models.BooleanField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.name