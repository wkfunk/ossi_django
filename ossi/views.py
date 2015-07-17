# Create your views here.
from django.views.generic.edit import CreateView
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,get_list_or_404,render_to_response
from .models import Breeder,ApprovedVariety,Variety,Seller,FAQ,VarietyFilter,Member
from django.forms.models import modelformset_factory
from ossi.forms import MemberForm,VarietyForm


def index(request):
    varieties = ApprovedVariety.objects.all().order_by('?')[:3]
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
#forms
def becomecontributor(request):
    if request.method == 'POST':
        formset = VarietyForm(request.POST,request.FILES)
        if formset.is_valid():
            formset.save()
            return render(request, 'ossi/becomecontributor.html', {'success':True})
    else:
        formset = VarietyForm()
    return render(request, "ossi/becomecontributor.html", {"formset":formset,})
def becomepartner(request):
    return render(request, 'ossi/members.html')
def becomemember(request):
    if request.method == 'POST':
        formset = MemberForm(request.POST)
        if formset.is_valid():
            formset.save()
            return render(request, 'ossi/becomemember.html', {'success':True})
    else:
        formset = MemberForm()
    return render(request, "ossi/becomemember.html", {"formset":formset,})
