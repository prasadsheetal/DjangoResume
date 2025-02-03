from django.shortcuts import render
from .models import Developer

def home(request):
    developer = Developer.objects.first()  # Adjust as needed
    return render(request, 'base/home.html', {'developer': developer})
