from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^faq', views.faq, name='about'),
    url(r'^news', views.news, name='about'),
    url(r'^resources', views.resources, name='about'),
    url(r'^seeds', views.seeds, name='about'),
    url(r'^partners', views.partners, name='about'),
    url(r'^team', views.team, name='about'),
    ]

