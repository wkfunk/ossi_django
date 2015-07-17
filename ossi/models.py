from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import django_filters
from django_filters import AllValuesFilter,ChoiceFilter,MultipleChoiceFilter,FilterSet,CharFilter
from django_filters.widgets import LinkWidget
from django.forms import ModelForm
from address.models import AddressField

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #address = models.ForeignKey('Address')
    address = AddressField(null=True)
    email = models.EmailField()
    def __str__(self):
        return ' '.join([self.first_name, self.last_name])

class Breeder(models.Model):
    name = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=50)
    #address = models.OneToOneField(Address)
    default_url = models.URLField(blank=True)
    email = models.EmailField()
    #phone = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.FileField()
    def __str__(self):
        return self.name + " (" + self.affiliation + ")"


class ApprovedVarietyManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedVarietyManager, self).get_queryset().filter(active=True)

class Variety(models.Model):
    #MODERATED
    #----------------------------
    name = models.CharField(max_length=50)
    crop_common_name = models.CharField(max_length=100)
    crop_latin_name = models.CharField(max_length=50)
    image = models.FileField(null=True)
    breeder = models.ForeignKey('Breeder',null=True)
    active = models.BooleanField(default=False)
    description = models.TextField()

    #SUBMISSIONS
    #----------------------------
    #variety contributor
    breeder_name = models.CharField(max_length=100, blank=True)
    breeder_affiliation = models.CharField(max_length=100, blank=True)
    breeder_address = AddressField(null=True, blank=True)
    breeder_email = models.EmailField(blank=True)

    #variety information
    sold_commercially = models.BooleanField(blank=True)
    where_sold_commercially = models.TextField(blank=True)

    #origin
    origin_population = models.TextField(blank=True)
    origin_parents = models.TextField(blank=True)
    origin_characteristics = models.TextField(blank=True)
    origin_two_or_more = models.BooleanField(blank=True)
    origin_selection_stabilization = models.BooleanField(blank=True)
    origin_single_parent = models.BooleanField(blank=True)
    breeding_crosses = models.TextField(blank=True)
    breeding_goals = models.TextField(blank=True)
    breeding_processes = models.TextField( blank=True)
    breeding_generations = models.IntegerField(null=True, blank=True)
    breeding_differ = models.TextField(blank=True)

    #stability
    stability = models.CharField(max_length=100, blank=True)
    submission_IP = models.BooleanField(blank=True)
    submission_IP_details = models.TextField(blank=True)
    submission_sole_breeder = models.BooleanField(blank=True)
    submission_sole_breeder_details = models.TextField(blank=True)
    submission_permission = models.BooleanField(blank=True)
    submission_permission_details = models.TextField(blank=True)
    submission_signature = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class ApprovedVariety(Variety):
    objects = ApprovedVarietyManager()
    class Meta:
        proxy = True


class Seller(models.Model):
    name = models.CharField(max_length=100)
    default_url = models.URLField()
    image = models.FileField()
    def __str__(self):
        return self.name

class SeedSold(models.Model):
    variety = models.ForeignKey('Variety',blank=True,null=True,related_name='locations')
    seller = models.ForeignKey('Seller')
    url = models.URLField()
    def __str__(self):
        return str(self.seller) + " (" + self.url + ")"

#PHONES
class Phone(models.Model):
    number = models.CharField(max_length=50)

    #reverse inline stuff
    # http://stackoverflow.com/questions/8597960/reverse-inlines-in-django-admin-with-more-than-one-model
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    of = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.number

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class VarietyFilter(FilterSet):
    crop_common_name = AllValuesFilter('crop_common_name',widget=LinkWidget)
    crop_latin_name = AllValuesFilter('crop_latin_name', widget=LinkWidget)
    breeder = AllValuesFilter('breeder__name', widget=LinkWidget)
    name = CharFilter('name', label='Search', lookup_type='icontains')

    class Meta:
        model = ApprovedVariety
        fields = ['breeder', 'crop_latin_name', 'crop_common_name', 'name']
