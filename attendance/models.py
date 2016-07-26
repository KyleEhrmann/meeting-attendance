from django.db import models


# Create your models here.
class Person(models.Model):

	name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=12)
	email_address = models.CharField(max_length=255)
	date_of_meeting = models.DateField()
	attended = models.BooleanField()

	def save(self):
		self.save()

	def __str__(self):
		return self.name