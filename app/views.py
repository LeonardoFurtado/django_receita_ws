from django.shortcuts import render
from .models import Company, ServiceOrder
from .forms import SearchModelForm


def list_companies(request):
    form = SearchModelForm(request.POST)

    if form.is_valid():
        companies = Company.objects.filter(
            name__icontains=form.cleaned_data['name'],
            uf__icontains=form.cleaned_data['uf'],
            email__icontains=form.cleaned_data['email']
        )
    else:
        companies = Company.objects.all()

    return render(request, 'companies.html', {'companies': companies, 'form': form})