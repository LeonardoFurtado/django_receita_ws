from django.shortcuts import render, redirect
from .models import Company, ServiceOrder
from .forms import SearchModelForm, CompanyForm, ServiceModelForm


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


def create_company(request):
    form = CompanyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request, 'company-form.html', {'form': form})


def update_company(request, id):
    company = Company.objects.get(id=id)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request, 'company-form.html', {'form': form, 'company':company})


def delete_company(request, id):
    company = Company.objects.get(id=id)

    if request.method == 'POST':
        company.delete()
        return redirect('list_companies')

    return render(request, 'company-delete-confirm.html', {'company': company})


def list_service_orders(request, company_id):
    services_orders = ServiceOrder.objects.all().filter(company_id=company_id)
    return render(request, 'service-orders.html', {'services_orders': services_orders})


def create_service_order(request):
    form = ServiceOrderModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request, 'service-orders-form.html', {'form': form})


def create_service(request):
    form = ServiceModelForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request, 'service-form.html', {'form': form})
