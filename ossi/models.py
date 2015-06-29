from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
import django_filters
from django_filters import AllValuesFilter,ChoiceFilter,MultipleChoiceFilter,FilterSet,CharFilter
from django_filters.widgets import LinkWidget

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #address = models.ForeignKey('Address')
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

class Variety(models.Model):
    name = models.CharField(max_length=50)
    crop = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    image = models.FileField()
    breeder = models.ForeignKey('Breeder')
    def __str__(self):
        return self.name

class VarietySubmission(models.Model):
    #variety contributor
    breeder = models.CharField(max_length=100)
    breeder_affiliation = models.CharField(max_length=100)
    #breeder_address = models.ForeignKey('Address')
    breeder_email = models.EmailField()
    #breeder_phone = models.CharField(max_length=50)

    #variety information
    crop_common_name = models.CharField(max_length=100)
    crop_latin_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    sold_commercially = models.BooleanField()
    where_sold_commercially = models.TextField()

    #origin
    origin_population = models.TextField()
    origin_parents = models.TextField()
    origin_characteristics = models.TextField()
    origin_two_or_more = models.BooleanField()
    origin_selection_stabilization = models.BooleanField()
    origin_single_parent = models.BooleanField()
    breeding_crosses = models.TextField()
    breeding_goals = models.TextField()
    breeding_processes = models.TextField()
    breeding_generations = models.IntegerField()
    breeding_differ = models.TextField()

    #stability
    stability = models.CharField(max_length=100)
    submission_IP = models.BooleanField()
    submission_IP_details = models.TextField()
    submission_sole_breeder = models.BooleanField()
    submission_sole_breeder_details = models.TextField()
    submission_permission = models.BooleanField()
    submission_permission_details = models.TextField()
    submission_signature = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " (" + self.breeder + ")"

class Seller(models.Model):
    name = models.CharField(max_length=100)
    default_url = models.URLField()
    image = models.FileField()
    sold = models.ForeignKey('SeedSold')
    def __str__(self):
        return self.name

class SeedSold(models.Model):
    location = models.ForeignKey('Seller')
    url = models.URLField()
    def __str__(self):
        return self.variety + " (" + self.seller + ")"


#ADDRESSES
class Address(models.Model):
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    #reverse inline stuff
    # http://stackoverflow.com/questions/8597960/reverse-inlines-in-django-admin-with-more-than-one-model
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    of = generic.GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return ', '.join([self.address_1, self.city, self.state])


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
    crop = AllValuesFilter('crop',widget=LinkWidget)
    latin_name = AllValuesFilter('latin_name', widget=LinkWidget)
    breeder = AllValuesFilter('breeder__name', widget=LinkWidget)
    name = CharFilter('name', label='Search', lookup_type='icontains')

    class Meta:
        model = Variety
        fields = ['breeder', 'latin_name', 'crop', 'name']
