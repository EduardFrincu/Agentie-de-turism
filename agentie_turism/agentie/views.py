from django.shortcuts import render, redirect
from .models import Client, Transport,Responsabil,Pachet_Turistic,Destinatie, Hotel
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import TripForm, CreateUserForm, HiddenForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




# Create your views here.
def index(request):
    num_clients = Client.objects.all().count()
    num_destinations = Destinatie.objects.all().count()

    Places = Destinatie.objects.values('Nume_Destinatie').distinct().all()
    num_places = Places.count()

    Towns = Destinatie.objects.distinct().all()
    Places_list = []

    for p in Places:
        Places_list.append( *p.values())

    Packs = Pachet_Turistic.objects.values('Tip_Pachet').distinct()
    form = TripForm(auto_id=False)

    Hidden_form = HiddenForm()


    context = { 'num_clients': num_clients,
                'num_destinations': num_destinations,
                'Places': Places,
                'Packs': Packs,
                'num_places': num_places,
                'form': form,
                'Places_list': Places_list,
                'Towns': Towns,
                'Hidden_form': Hidden_form,
                }


    return render(request, 'index.html', context = context)

def destinatie(request):
    emails = User.objects.filter(is_active=True).values_list('email', flat=True)
    context = {}
    if request.method == 'POST':
        form = TripForm(request.POST)

        if form.is_valid():
            destinatie_post = form.cleaned_data["Destinatie"]
            transport_post = form.cleaned_data["Transport"]
            plecare_post = form.cleaned_data["Plecare"]
            data_plecare_post = form.cleaned_data["Data_plecare"]

            Places = Hotel.objects.select_related('Destinatie').filter(Destinatie__Nume_Destinatie = destinatie_post)
            form_completed = Places.exists()

            context = {
                'destinatie_post': destinatie_post,
                'transport_post': transport_post,
                'plecare_post': plecare_post,
                'data_plecare_post': data_plecare_post,
                'Places':Places,
                'emails':emails,
                'form_completed': form_completed,

            }
        else:
            form_completed = False
            Hoteluri = Hotel.objects.all()
            if request.method == 'POST':
                form = HiddenForm(request.POST)
                if form.is_valid():
                    value = form.cleaned_data["value"]
                    context = {
                        'value': value,

                    }



    return render(request, 'agentie/destinatie_list.html', context = context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Username sau parola gresite')

    context = {}

    return render(request, 'accounts/login.html', context = context)

def logoutPage(request):
    logout(request)
    return redirect('/')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            nume = form.cleaned_data.get('nume')
            prenume = form.cleaned_data.get('prenume')

            is_registered = Client.objects.filter(Email = email).exists()

            if(is_registered == False):
                p = Client.objects.create(Nume = nume, Prenume = prenume)



            messages.success(request, 'Cont creat pentru ' + user)
            return redirect('login')

    context = {'form': form,
               }

    return render(request, 'accounts/register.html', context = context)

@login_required(login_url='login')
def my_account(request):
    context = {}

    email = request.user.email

    client = Client.objects.get(Email = email)
    Responsabil = client.Responsabil.Nume_Responsabil
    user_logat = client
    Pachet_Turistic1 =[]

    aux = Pachet_Turistic.objects.all().prefetch_related('Client').filter(Client__Email = email)


    for pachet in aux:
        Pachet_Turistic1.append(((pachet.Tip_Pachet) ,(pachet.id),(pachet.Zi_inceput),(pachet.Zi_sfarsit)))


    ceva =list(zip(*Pachet_Turistic1))
    ids = ceva[1]

    destinatie = []

    for i in ids:
        aux = Pachet_Turistic.objects.get(id = i)
        destinatie.append((aux.id,aux.Destinatie.Nume_Destinatie, aux.Destinatie.Oras))


    ceva = list(zip(*destinatie))
    orase = ceva[0]

    hoteluri = []

    querry = Hotel.objects.raw("SELECT H.Nume_Hotel, H.id FROM agentie_hotel H  INNER JOIN agentie_destinatie D ON D.id = H.Destinatie_id INNER JOIN agentie_pachet_turistic PT ON PT.Destinatie_id = D.id INNER JOIN agentie_pachet_turistic_client PTC ON PTC.pachet_turistic_id = PT.id INNER JOIN agentie_client C ON PTC.client_id = C.id WHERE Nume = 'Sava' ")

    for hotel in querry:
        hoteluri.append(hotel.Nume_Hotel)

    Data_sheet = zip(Pachet_Turistic1, destinatie, hoteluri)


    context = {'email': email,
               'Responsabil': Responsabil,
               'user_logat': user_logat,
               'Data_sheet': Data_sheet,
               'hoteluri':hoteluri,
               }

    return render(request, 'accounts/my_account.html', context = context)

def rezervare(request):
    context = {}

    return render(request, 'agentie/rezervare.html', context = context)
