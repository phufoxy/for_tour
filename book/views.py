from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Book_Tour,Restaurant_tour,Place_tour,Vehicle_tour,House_tour,Book_Tour_Details,Album_Tour
from tourer.models import Tourer, Account
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from tour.models import Tour,PlaceTour,BookTour
# Create your views here.
def book(request):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
    context = {
        'idempresa':idempresa
    }
    return render(request,'home/book/book.html',context)


def book_details(request):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    if idempresa == None:
        return redirect('/login/?next=' + request.path)
    else:
        account = Account.objects.get(email=idempresa)
        query = "SELECT t.*,b.*,sum(p.price) as total_price,(sum(p.price) * t.person) as sum_price FROM tour_tour t  inner join tour_placetour p on t.id=p.tour_id inner join  tour_booktour b on b.tour_id = t.id where b.accout_id =  '" + str(account.id) + "'" +" group by t.id"
        book_Tour = BookTour.objects.raw(query)
        book_Tour_count = BookTour.objects.filter(accout=account).count()
        if book_Tour_count == 0 :
            context = {
                'idempresa':idempresa
            }
            return render(request,'error/index.html',{
                'error':'You Not Tour , please choose tour'
            })
        else:
            context = {
                'idempresa':idempresa,
                'context':book_Tour
            }
            return render(request,'home/book/book_details.html',context)
    

def book_details_to(request,id):
    book_Tour = Book_Tour.objects.get(pk=id)
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
    
    datenow = datetime.now()
    place_tour = Place_tour.objects.filter(book=book_Tour).filter(date_to__range=[datetime.now(),'2020-1-1']).order_by('date_to')
    count_place = Place_tour.objects.filter(book=book_Tour).count()
    house_tour = House_tour.objects.filter(book=book_Tour)
    count_house = House_tour.objects.filter(book=book_Tour).count()
    restaurant_tour = Restaurant_tour.objects.filter(book=book_Tour)
    count_restaurant_tour = Restaurant_tour.objects.filter(book=book_Tour).count()
    vehicle_tour = Vehicle_tour.objects.filter(book=book_Tour)
    vehicle_tour_count = Vehicle_tour.objects.filter(book=book_Tour).count()
    tourer = Account.objects.filter(email=idempresa)
    context = {
        'idempresa':idempresa,
        'book_Tour':book_Tour,
        'place_tour':place_tour,
        'count_place':count_place,
        'house_tour':house_tour,
        'count_house':count_house,
        'restaurant_tour':restaurant_tour,
        'count_restaurant_tour':count_restaurant_tour,
        'vehicle_tour':vehicle_tour,
        'vehicle_tour_count':vehicle_tour_count,
        'tourer':tourer
    }
    return render(request,'home/book/book_details_to.html',context)

def delete_book(request,id):
    book_Tour=Book_Tour.objects.get(pk=id)
    book_Tour.delete()
    return redirect('book_details')

def create_book(request):
    name_book = request.GET['name_book']
    date_book = request.GET['date_book']
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        try:
            account_details = Account.objects.get(email=idempresa)
            book_Tour = Book_Tour(name_book=name_book,date_book=datetime.now(),date_start=date_book,tourer=account_details)
            book_Tour.save()
            return redirect('book_details')
        except Exception as e:
            print(e)
            return redirect('book')

def album(request,id):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        book_Tour = Book_Tour.objects.get(pk=id)
        album_Tour = Album_Tour.objects.filter(book=id)
        context = {
            'book_Tour':book_Tour,
            'album_Tour':album_Tour
        }
        return render(request,'home/book/album.html',context)

def upload_album(request,id):
    book_Tour = Book_Tour.objects.get(pk=id)
    if request.method == 'POST' and request.FILES['myFile']:
        myFile =   request.FILES['myFile']
        fs =  FileSystemStorage()
        filename = fs.save(myFile.name,  myFile)
        uploaded_file_url = fs.url(filename)
        album_Tour = Album_Tour(book=book_Tour,img_album=uploaded_file_url.strip('/media'),date_up=datetime.now())
        album_Tour.save()
        return redirect('album',id=id)

class ListTourer(generic.ListView):
    template_name = "dashboard/account/table.html"
    context_object_name = 'context'
    paginate_by = 8
    def get_queryset(self):
        return Account.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListTourer, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListTourer, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddTourer(CreateView):
    template_name = 'dashboard/account/form.html'
    model = Account
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')

    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddTourer, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddTourer, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddTourer, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx
    

        
class UpdateTourer(UpdateView):
    template_name = 'dashboard/account/form.html'
    model = Account
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House') #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        # super(UpdateHouse, self).form_valid(form)
        return super(UpdateTourer, self).form_valid(form)


    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateTourer, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateTourer, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteTourer(DeleteView):
    model = Account
    success_url = reverse_lazy('ListTourer')