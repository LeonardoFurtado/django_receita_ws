from django import forms
from .models import Company, ServiceOrder, Service
from localflavor.br.br_states import STATE_CHOICES


class SearchModelForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    uf = forms.ChoiceField(choices=STATE_CHOICES, required=False, initial={None: '----'})
    email = forms.EmailField(max_length=100, required=False)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'uf', 'email', 'services']


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title']


class ServiceOrderModelForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = ['title', 'company', 'service']