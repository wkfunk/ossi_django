from django import forms
from address.forms import AddressField
from .models import Member

class MemberForm(forms.ModelForm):
    #first_name = forms.CharField(label="First name", max_length=100)
    #last_name = forms.CharField(label="Last name", max_length=100)
    #email = forms.EmailField()
    #address = AddressField()
    class Meta:
        model = Member
        exclude = []
    
