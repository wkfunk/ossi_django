from django.contrib import admin
from .models import Member,Breeder,Variety,VarietySubmission,Seller,SeedSold

admin.site.register(Member)
admin.site.register(Breeder)
admin.site.register(Variety)
admin.site.register(VarietySubmission)
admin.site.register(Seller)
admin.site.register(SeedSold)
