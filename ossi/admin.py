from django.contrib import admin
from .models import Member,Breeder,Variety,Seller,SeedSold,Phone,FAQ
from django.contrib.contenttypes import generic


# ex input 
    #(None,
        #{'fields':('title', 'content')}
    #)
# output
   #(None,
        #{'fields':('title',)}
    #),
    #('Extra',
        #{
            #'fields':  ('content',),
            #'classes':('collapse',),
        #}
    #),
#http://stackoverflow.com/questions/2420516/how-to-collapse-just-one-field-in-django-admin
def hide_fields(start_tuple):
        all_fields = [f.name for f in Variety._meta.fields if not f.auto_created]
        show_fields = start_tuple[1]['fields']
        remaining_fields = [f for f in all_fields if f not in show_fields]
        return (start_tuple, ('Extra', {'fields': tuple(remaining_fields), 'classes': ('collapse'),}),)
    

#inlines
class PhoneInLine(generic.GenericStackedInline):
    model = Phone
    max_num = 1
class SeedSoldInline(admin.TabularInline):
    model = SeedSold
    extra = 1

#admins
class BreederAdmin(admin.ModelAdmin):
    model = Breeder

class VarietyAdmin(admin.ModelAdmin):
    model = Variety
    inlines = [
            SeedSoldInline,
            ]
    fieldsets = hide_fields(
            ('Publicly visible fields', {'fields': ['name', 'crop_common_name', 'crop_latin_name', 'image', 'breeder', 'description', 'active']})
)
    

admin.site.register(Member)
admin.site.register(Breeder,BreederAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(Seller)
admin.site.register(SeedSold)
admin.site.register(Phone)
admin.site.register(FAQ)
