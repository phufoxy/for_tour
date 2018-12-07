from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Place,PlaceDetails,CommentPlace
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tourer.models import Tourer
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from book.models import Book_Tour,Place_tour
from django.views.generic import TemplateView
from .forms import PlaceForm
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.contrib.messages.views import SuccessMessageMixin

# Place Index
class Index(generic.ListView):
    model = Place
    context_object_name = 'context'
    template_name = 'dashboard/places/places/index.html'

# Create
class PlaceCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'dashboard/places/places/create_place.html'
    form_class = PlaceForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('ListPlace')


# Delete
class PlaceDeleteView(DeleteAjaxMixin, generic.DeleteView):
    model = Place
    template_name = 'dashboard/places/places/delete_place.html'
    success_message = 'Success: Place was deleted.'
    success_url = reverse_lazy('ListPlace')



# Create your views here.
# Form add
class AddEmail(CreateView):
    template_name = 'dashboard/places/index.html'
    fields = '__all__'
    #urls name
    def get(self,request):
        form = PlaceForm()
        return render(request,self.template_name,{'form':form})
  

def index(request):
    place = Place.objects.order_by('-id')
    city = Place.objects.values('city').distinct()
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
        'place':users,
        'city':city
    }
    return render(request,'home/places/places.html',context)

def search_form(request):
    if request.method == "POST": 
        name = request.POST['city']
        if name == "all":
            return redirect('/places')
        else :
            return redirect('/places/search/'+name)
   

def search_place(request,name):
    place = Place.objects.filter(city=name)
    city = Place.objects.values('city').distinct()

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
        'place':users,
        'city':city
    }
    return render(request,'home/places/places.html',context)

def places_details(request,id):
    try:
        places_details = Place.objects.get(pk=id)
        places_details.review = places_details.review + 1
        places_details.save()
        idempresa= ''
        if 'account' in request.session:
            idempresa = request.session['account']
        else:
            idempresa=None

        if idempresa == None:
            return redirect('/login/?next='+ request.path)
        else:
            tourer = Tourer.objects.filter(email=idempresa)
            places_items = PlaceDetails.objects.filter(place=id)
            sum_commnet = CommentPlace.objects.filter(place=id).count()
            comment = CommentPlace.objects.filter(place=id)
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
    except Place.DoesNotExist as e:
        return render(request,'error/index.html',{
            'error':'wrong routing path'
        })
    # account
    

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
            comment_place = CommentPlace(place=place_details,comment=commnet_items,date=datetime.now(),account=account_details)
            comment_place.save()
            return redirect('places_details',id=id)
        except Exception as e:
            print(e)
            return redirect('places_details',id=id)

class ListPlace(generic.ListView):
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
            ctx = super(ListPlace, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListPlace, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

# Form add
class AddPlace(CreateView):
    template_name = 'dashboard/places/places/table.html'
    model = Place
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddPlace, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddPlace, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddPlace, self).get_context_data(**kwargs)
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

class DeletePlace(DeleteView):
    model = Place
    success_url = reverse_lazy('ListPlace')

# places details
class ListPlaceDetails(generic.ListView):
    template_name = "dashboard/places/places_details/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return PlaceDetails.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListPlaceDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListPlaceDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddPlaceDetails(CreateView):
    template_name = 'dashboard/places/places_details/form.html'
    model = PlaceDetails
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddPlaceDetails, self).form_valid(form)

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddPlaceDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddPlaceDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdatePlaceDetails(UpdateView):
    template_name = 'dashboard/places/places_details/form.html'
    model = PlaceDetails
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdatePlaceDetails, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdatePlaceDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdatePlaceDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeletePlaceDetails(DeleteView):
    model = PlaceDetails
    success_url = reverse_lazy('ListPlaceDetails')
