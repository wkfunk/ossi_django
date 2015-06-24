from django.contrib import admin
from .models import Member,Breeder,Variety,VarietySubmission,Seller,SeedSold,Phone,Address,BreederPhone,BreederAddress


#inlines
class BreederAddressInLine(admin.StackedInline):
    model = BreederAddress
    extra = 1

class BreederPhoneInline(admin.StackedInline):
    model = BreederPhone
    extra = 1

#admins
class BreederAdmin(admin.ModelAdmin):
    inlines = [
            BreederAddressInLine,
            BreederPhoneInline,
            ]

    
admin.site.register(Member)
admin.site.register(Breeder,BreederAdmin)
admin.site.register(Variety)
admin.site.register(VarietySubmission)
admin.site.register(Seller)
admin.site.register(SeedSold)
admin.site.register(Phone)
admin.site.register(Address)
