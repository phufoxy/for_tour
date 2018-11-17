from django.shortcuts import render
from places.models import Place
from house.models import House
# Create your views here.
def home(request):
    places = Place.objects.all().order_by('-id')[:8]
    houses = House.objects.all().order_by('-id')[:3]
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
    context = {
        'places':places,
        'idempresa':idempresa,
        'houses':houses
    }
    return render(request,'home/home.html',context)