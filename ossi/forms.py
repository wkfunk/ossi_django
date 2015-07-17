from django import forms
from address.forms import AddressField
from .models import Member,Variety
from django.forms.fields import BooleanField

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = []
    
class VarietyForm(forms.ModelForm):
    class Meta:
        model = Variety
        exclude = ['breeder', 'active']
    #http://stackoverflow.com/questions/1134667/django-required-field-in-model-form
    def __init__(self, *args, **kwargs):
        super(VarietyForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            if not isinstance(self.fields[key], BooleanField):
                self.fields[key].required = True
