from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    email = models.EmailField()

class Breeder(models.Model):
    name = models.CharField(max_length=50)
    affiliation = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    bio = models.TextField()
    # need to setup ImageField
    image = models.CharField(max_length=50)

class Variety(models.Model):
    name = models.CharField(max_length=50)
    crop = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    # need to setup ImageField
    image = models.CharField(max_length=50)
    breeder = models.ForeignKey('Breeder')

class VarietySubmission(models.Model):
    name = models.CharField(max_length=50)
    crop = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50)
    # need to setup ImageField
    image = models.CharField(max_length=50)
    breeder = models.ForeignKey('Breeder')
    sold_commercially = models.BooleanField()
    where_sold_commercially = models.TextField()
    origin_population = models.CharField(max_length=100)
    origin_parents = models.CharField(max_length=100)
    origin_characteristics = models.TextField()
    origin_two_or_more = models.BooleanField()
    origin_selection_stabilization = models.BooleanField()
    origin_single_parent = models.BooleanField()
    breeding_crosses = models.IntegerField()
    breeding_goals = models.TextField()
    breeding_processes = models.TextField()
    breeding_generations = models.IntegerField()
    breeding_differ = models.BooleanField()
    stability = models.BooleanField()
    submission_IP = models.BooleanField()
    submission_IP_details = models.TextField()
    submission_sole_breeder = models.BooleanField()
    submission_sole_breeder_details = models.TextField()
    submission_permission = models.BooleanField()
    submission_signature = models.CharField(max_length=100)

class Seller(models.Model):
    name = models.CharField(max_length=100)
    default_url = models.URLField()
    # need to setup ImageField
    image = models.CharField(max_length=50)

class SeedSold(models.Model):
    seller = models.ForeignKey('Seller')
    variety = models.ForeignKey('Variety')
    url = models.URLField()

