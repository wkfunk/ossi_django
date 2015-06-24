# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import Breeder

def index(request):
    return render(request, 'ossi/index.html')

def about(request):
    return render(request, 'ossi/about.html')

def faq(request):
    return render(request, 'ossi/faq.html')
def news(request):
    return render(request, 'ossi/news.html')
def resources(request):
    return render(request, 'ossi/resources.html')
def seeds(request):
    return render(request, 'ossi/seeds.html')
def partners(request):
    return render(request, 'ossi/partners.html')
def team(request):
    return render(request, 'ossi/team.html')
def breeders(request):
    breeders = get_list_or_404(Breeder)
    return render(request, 'ossi/breeders.html', {'breeders':breeders})
def members(request):
    return render(request, 'ossi/members.html')
