from django.shortcuts import render, redirect, HttpResponseRedirect
from places.models import Place
from house.models import House
from tour.models import Tour,BookTour
from tourer.models import Tourer, Account
from django.contrib import messages

# Create your views here.
def home(request):
    places = Place.objects.all().order_by('-id')[:8]
    houses = House.objects.all().order_by('-id')[:3]
    query = "SELECT *,(sum(a.price) * t.person) as sum_price, sum(a.price) as total_price FROM tour_placeTour a inner join tour_tour t on a.tour_id  = t.id group by t.id  limit 8"
    tour = Tour.objects.raw(query)
    
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    account = "None"

    try:
        account = Account.objects.get(email=idempresa)
        author_account = account.author
        if author_account == 'admin':
            query_details = "SELECT t.*,b.*,sum(p.price) as total_price,(sum(p.price) * t.person) as sum_price FROM tour_tour t  inner join tour_placetour p on t.id=p.tour_id inner join  tour_booktour b on b.tour_id = t.id where b.accout_id =  '" + str(account.email) + "'" +" group by t.id"
            bookTour = BookTour.objects.raw(query_details)
            tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")

            context = {
                'context':tour,
                'idempresa':idempresa,
                'houses':houses,
                'bookTour':bookTour,
                'tour_city':tour_city,
                'admin':'admin',            
            }
            return render(request,'home/home.html',context)
        else:
            query_details = "SELECT t.*,b.*,sum(p.price) as total_price,(sum(p.price) * t.person) as sum_price FROM tour_tour t  inner join tour_placetour p on t.id=p.tour_id inner join  tour_booktour b on b.tour_id = t.id where b.accout_id =  '" + str(account.email) + "'" +" group by t.id"
            bookTour = BookTour.objects.raw(query_details)
            tour_city = Tour.objects.raw("SELECT  city,id from tour_tour group by city")

            context = {
                'context':tour,
                'idempresa':idempresa,
                'houses':houses,
                'bookTour':bookTour,
                'tour_city':tour_city,
            }
            return render(request,'home/home.html',context)
    except Exception as e:
        messages.error(request, 'Page Error'  + e)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
  

def search_multi(request):
    if request.method == "POST":
        city = request.POST.get('city_tour')
        price = request.POST.get('price')
        person = request.POST.get('person')
        date = request.POST.get('date')
        return redirect('/tour/search/' + city + '/' + str(price) + '/' + str(person) + '/' + str(date) + '/')
    else:
        return render(request,'error/index.html',{
            'error':'wrong routing path'
        })