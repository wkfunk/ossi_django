from django.contrib import admin
from .models import Member,Breeder,Variety,VarietySubmission,Seller,SeedSold,Phone,Address,FAQ
from django.contrib.contenttypes import generic


#inlines
class AddressInLine(generic.GenericStackedInline):
    model = Address
    max_num = 1
class PhoneInLine(generic.GenericStackedInline):
    model = Phone
    max_num = 1
class SeedSoldInline(admin.TabularInline):
    model = SeedSold
    extra = 1

#admins
class BreederAdmin(admin.ModelAdmin):
    model = Breeder
    inlines = [
            AddressInLine,
            ]

class VarietyAdmin(admin.ModelAdmin):
    model = Variety
    inlines = [
            SeedSoldInline,
            ]

admin.site.register(Member)
admin.site.register(Breeder,BreederAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(VarietySubmission)
admin.site.register(Seller)
admin.site.register(SeedSold)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(FAQ)
