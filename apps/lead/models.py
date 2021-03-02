from django.db import models
from django.utils.translation import gettext_lazy as _


class Lead(models.Model):
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(max_length=20, verbose_name=_('Phone_number'))

    summ = models.CharField(max_length=100)
    years = models.CharField(max_length=100)
    agree = models.CharField(max_length=100)
    fio = models.CharField(max_length=100)
    personalCode = models.CharField(max_length=100)
    accommodation_type = models.CharField(max_length=100)
    summ_input = models.CharField(max_length=100)
    years_input = models.CharField(max_length=100)
    percented = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

    dependents = models.CharField(max_length=100)
    incomeType = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    credit_aim = models.CharField(max_length=100)
    familyType = models.CharField(max_length=100)
    living_city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    workType = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)

    vypiska_file = models.FileField(upload_to='lead_files/', null=True, blank=True)

