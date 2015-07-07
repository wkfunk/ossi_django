# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import Breeder,Variety,Seller,FAQ,VarietyFilter

def index(request):
    varieties = Variety.objects.all().order_by('?')[:3]
    return render(request, 'ossi/index.html', {'varieties':varieties})

def about(request):
    return render(request, 'ossi/about.html')

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'ossi/faq.html', {'faqs':faqs})
def news(request):
    return render(request, 'ossi/news.html')
def resources(request):
    return render(request, 'ossi/resources.html')
def seeds(request):
    #varieties = get_list_or_404(Variety)
    varieties = VarietyFilter(request.GET)
    return render(request, 'ossi/seeds.html', {'varieties':varieties})
def partners(request):
    #partners = get_list_or_404(Seller)
    partners = Seller.objects.all().order_by('name')
    return render(request, 'ossi/partners.html', {'partners':partners})
def team(request):
    return render(request, 'ossi/team.html')
def breeders(request):
    #breeders = get_list_or_404(Breeder)
    breeders = Breeder.objects.all().order_by('name')
    return render(request, 'ossi/breeders.html', {'breeders':breeders})
def members(request):
    return render(request, 'ossi/members.html')
