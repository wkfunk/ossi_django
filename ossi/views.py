# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("index")

def about(request):
    return HttpResponse("about")

def faq(request):
    return HttpResponse("faq")
def news(request):
    return HttpResponse("news")
def resources(request):
    return HttpResponse("resources")
def seeds(request):
    return HttpResponse("seeds")
def partners(request):
    return HttpResponse("partners")
def team(request):
    return HttpResponse("team")
