from django.db import models
from localflavor.br.br_states import STATE_CHOICES


class Base(models.Model):
    """Base class used to load these attributes in all models."""
    creation_date = models.DateField('Creation date', auto_now_add=True)
    updated = models.DateField('Update date', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)

    class Meta:
        abstract = True


class Service(Base):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Company(Base):
    name = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=100)
    services = models.ManyToManyField(Service, blank=True)

    def __str__(self):
        return self.name


class ServiceOrder(Base):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
