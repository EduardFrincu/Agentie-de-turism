import uuid
from datetime import date
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    Nume = models.CharField(max_length =  30)
    Prenume = models.CharField(max_length = 30)
    Telefon = models.IntegerField(blank=True, null = True)
    Email = models.EmailField(max_length=35, blank=True, null = True)
    Responsabil = models.ForeignKey('Responsabil', on_delete=models.CASCADE, blank=True, null = True)

    class Meta:
        ordering = ['Nume', 'Prenume']

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.Nume, self.Prenume)


class Responsabil (models.Model):
    Nume_Responsabil = models.CharField(max_length = 30)
    Prenume_Responsabil = models.CharField(max_length = 30)
    Telefon_Responsabil = models.IntegerField()
    Email_Responsabil = models.EmailField(max_length=35, null=True)
    Salariu = models.DecimalField(max_digits = 8, decimal_places=2)

    def __str__(self):
        return '{0}, {1}'.format(self.Nume_Responsabil, self.Prenume_Responsabil)

class Destinatie(models.Model):
    Nume_Destinatie = models.CharField(max_length=30)
    Oras = models.CharField(max_length=20)

    def get_Nume(self):
        return self.Nume_Destinatie

    def __str__(self):
        return '{0}, {1}'.format(self.Nume_Destinatie, self.Oras)

class Pachet_Turistic(models.Model):
    Tip_Pachet = models.CharField(max_length=30)
    Zi_inceput = models.DateField()
    Zi_sfarsit = models.DateField()
    Client = models.ManyToManyField(Client, blank = True)
    Destinatie = models.ForeignKey(Destinatie, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.Tip_Pachet


class Plecare(models.Model):
    Nume_locatie = models.CharField(max_length = 30)
    Destinatie = models.ManyToManyField(Destinatie, blank=True)

    def __str__(self):
        return  '{0}' .format(self.Nume_locatie)


class Transport(models.Model):
    Tip_Transport = models.CharField(max_length=20)
    Destinatie = models.ManyToManyField(Destinatie)

    def __str__(self):
        return self.Tip_Transport


class Hotel(models.Model):
    Nume_Hotel = models.CharField(max_length = 20)
    Pret_noapte = models.IntegerField()
    Check_in = models.DateField()
    Check_out = models.DateField()
    Nr_Camere = models.IntegerField()
    Destinatie = models.ForeignKey(Destinatie, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{0}, {1}' .format(self.Nume_Hotel, self.Destinatie)





