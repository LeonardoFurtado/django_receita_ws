from django import forms
from localflavor.br.br_states import STATE_CHOICES


class SearchModelForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    uf = forms.ChoiceField(choices=STATE_CHOICES, required=False, initial={None: '----'})
    email = forms.EmailField(max_length=100, required=False)