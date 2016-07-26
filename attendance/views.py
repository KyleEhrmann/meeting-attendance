from django.shortcuts import render
from django.utils import timezone
from .models import Person

# Create your views here.
def person_list(request):
	people = Person.objects.all()
	return render(request, 'attendance/person_list.html', {'people':people})