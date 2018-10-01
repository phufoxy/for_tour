from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Place,City,Place_details,Comment_place
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tourer.models import Tourer
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from book.models import Book_Tour,Place_tour
# Create your views here.
def index(request):
    place = Place.objects.select_related('location').order_by('-id')
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(place, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = { 
        'idempresa':idempresa,
        'place':users

    }
    return render(request,'home/places/places.html',context)

def places_details(request,id):
    places_details = Place.objects.get(pk=id)
    places_details.review = places_details.review + 1
    places_details.save()
    # account
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    if idempresa == None:
        return redirect('/login/?next='+ request.path)
    else:
        tourer = Tourer.objects.filter(email=idempresa)
        places_items = Place_details.objects.filter(place=id)
        sum_commnet = Comment_place.objects.filter(place=id).count()
        comment = Comment_place.objects.filter(place=id).order_by('-date')
        account = Tourer.objects.get(email=idempresa)
        book_Tour = Book_Tour.objects.filter(tourer=account).order_by('-id')
        # context
        context = {
            'idempresa':idempresa,
            'tourer':tourer,
            'places_items':places_items,
            'sum_commnet':sum_commnet,
            'comment':comment,
            'places_details':places_details,
            'book_Tour':book_Tour

        }
        return render(request,'home/places/places_details.html',context)

def create_place_tour(request,id):
    place_details = Place.objects.get(pk=id)
    # email = request.GET['email']
    book = request.GET['book']
    date_to = request.GET['date_to']
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        try:
            book_Tour = Book_Tour.objects.get(name_book=book)
            account_details = Tourer.objects.get(email=idempresa)
            place_tour = Place_tour(book=book_Tour,place=place_details,account=account_details,date_book=datetime.now(),date_to=date_to)
            place_tour.save()
            return redirect('places_details',id=id)
        except Exception as e:
            print(e)
            return redirect('places_details',id=id)


def create_comment_place(request,id):
    place_details = Place.objects.get(pk=id)
    # email = request.GET['email']
    commnet_items = request.GET['comment_items']
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    
    if idempresa == None:
        return redirect('login')
    else:
        try:
            account_details = Tourer.objects.get(email=idempresa)
            comment_place = Comment_place(place=place_details,commnet=commnet_items,date=datetime.now(),account=account_details)
            comment_place.save()
            return redirect('places_details',id=id)
        except Exception as e:
            print(e)
            return redirect('places_details',id=id)

class IndexView_Place(generic.ListView):
    template_name = "dashboard/places/places/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Place.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Place, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Place, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreatePlace(CreateView):
    template_name = 'dashboard/places/places/form.html'
    model = Place
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreatePlace, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreatePlace, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreatePlace, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdatePlace(UpdateView):
    template_name = 'dashboard/places/places/form.html'
    model = Place
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdatePlace, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdatePlace, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdatePlace, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class PlaceDelete(DeleteView):
    model = Place
    success_url = reverse_lazy('IndexView_Place')

# city
class IndexView_Place_City(generic.ListView):
    template_name = "dashboard/places/city/table.html"
    context_object_name = 'city'
    paginate_by = 12
    def get_queryset(self):
        return City.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Place_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Place_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreatePlace_City(CreateView):
    template_name = 'dashboard/places/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreatePlace_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreatePlace_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreatePlace_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdatePlace_City(UpdateView):
    template_name = 'dashboard/places/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdatePlace_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdatePlace_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdatePlace_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class PlaceDelete_City(DeleteView):
    model = City
    success_url = reverse_lazy('IndexView_Place_City')

# places details
class IndexView_Place_details(generic.ListView):
    template_name = "dashboard/places/places_details/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Place_details.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Place_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Place_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreatePlaces_details(CreateView):
    template_name = 'dashboard/places/places_details/form.html'
    model = Place_details
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')


   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreatePlaces_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreatePlaces_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreatePlaces_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdatePlaces_details(UpdateView):
    template_name = 'dashboard/places/places_details/form.html'
    model = Place_details
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')


   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdatePlaces_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdatePlaces_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdatePlaces_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class PlacesDelete_details(DeleteView):
    model = Place_details
    success_url = reverse_lazy('IndexView_House_details')
