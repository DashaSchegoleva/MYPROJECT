
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  Advertisement
from .forms import AdvertisementForm
# Create your views here.
def index(request):
    advertisments = Advertisement.objects.all()
    context = {'advertisments': advertisments}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisment = Advertisement(**form.cleaned_data)
            advertisment.user = request.user
            advertisment.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)