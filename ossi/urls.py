from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^faq', views.faq, name='faq'),
    url(r'^news', views.news, name='news'),
    url(r'^resources', views.resources, name='resources'),
    url(r'^seeds', views.seeds, name='seeds'),
    url(r'^partners', views.partners, name='partners'),
    url(r'^team', views.team, name='team'),
    url(r'^breeders', views.breeders, name='breeders'),
    url(r'^members', views.members, name='members'),
    ]

