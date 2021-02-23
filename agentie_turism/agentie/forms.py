from django import forms
import datetime
from .models import Destinatie, Plecare
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

Destinatii = Destinatie.objects.values('Nume_Destinatie').distinct()
Orase = Plecare.objects.values('Nume_locatie').distinct()

Destinatie_Choices = [( '', 'Destinatie')]
Orase_Choices = [( '', 'Plecare')]

for d in Destinatii:
    Destinatie_Choices.append((*d.values(),*d.values()))

for o in Orase:
    Orase_Choices.append((*o.values(),*o.values()))

Transport_Choices = [
    ( '', 'Transport'),
    ('Avion', 'Avion'),
    ('Autocar', 'Autocar'),
    ('Individual', 'Individual')
]

class TripForm(forms.Form):

    Destinatie = forms.CharField(label='', widget=forms.Select(choices=Destinatie_Choices), empty_value='Destinatie')
    Transport = forms.CharField(label='',widget=forms.Select(choices=Transport_Choices), empty_value='Transport')
    Plecare = forms.CharField(label='',widget=forms.Select(choices=Orase_Choices), empty_value='Plecare')
    Data_plecare = forms.DateField(label='',widget=forms.TextInput(attrs={'placeholder': 'Data plecare...'}), initial=datetime.date.today)

class BookingForm(forms.Form):
    Perioada = forms.CharField(label='', widget=forms.Select(choices=Destinatie_Choices), empty_value='Destinatie')

class HiddenForm(forms.Form):
    value = forms.CharField(widget=forms.HiddenInput())

class CreateUserForm(UserCreationForm):
    nume = forms.CharField(label = '', max_length=20)
    prenume = forms.CharField(label='', max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Nume utilizator..'})
        self.fields['nume'].widget.attrs.update({'placeholder': 'Nume..'})
        self.fields['prenume'].widget.attrs.update({'placeholder': 'Prenume..'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email..'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Parola..'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repetati parola..'})

    class Meta:
        model = User
        fields = ['username','nume', 'prenume', 'email', 'password1', 'password2']
