from django.shortcuts import render
from django.http import HttpResponse
from .models import  Advertisement
# Create your views here.
def index(request):
    advertisments = Advertisement.objects.all()
    context = {'advertisments': advertisments}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')