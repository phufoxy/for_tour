from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import City,House,House_details,Comment_house
from tourer.models import Tourer
from django.template import RequestContext
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from book.models import Book_Tour,Place_tour,House_tour

# Create your views here.
def house(request):
    house_items = House.objects.select_related('location').order_by('-id')
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(house_items, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {
        'house_items':users,
        'idempresa':idempresa

    }
    return render(request,'home/hotels.html',context)

def house_details(request,id):
    house_details = House.objects.get(pk=id)
    house_details.review = house_details.review + 1
    house_details.save()
    # house items
    house_items = House_details.objects.filter(house=id)
    # account
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    tourer = Tourer.objects.filter(email=idempresa)
    comment = Comment_house.objects.filter(house=id).order_by('-date')
    sum_commnet = Comment_house.objects.filter(house=id).count()
    account = Tourer.objects.get(email=idempresa)
    book_Tour = Book_Tour.objects.filter(tourer=account).order_by('-id')
    # context
    context = {
        'house_items':house_items,
        'idempresa':idempresa,
        'tourer':tourer,
        'house_details':house_details,
        'comment':comment,
        'sum_commnet':sum_commnet,
        'book_Tour':book_Tour

        # 'a':a
    }
    return render(request,'home/hotel_details.html',context)

def create_house_tour(request,id):
    house_details = House.objects.get(pk=id)
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
            house_tour = House_tour(book=book_Tour,house=house_details,account=account_details,date_book=datetime.now(),date_to=date_to)
            house_tour.save()
            return redirect('house_details',id=id)
        except Exception as e:
            print(e)
            return redirect('house_details',id=id)

def create_comment_house(request,id):
    house_details = House.objects.get(pk=id)
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
            comment_house = Comment_house(house=house_details,commnet=commnet_items,date=datetime.now(),account=account_details)
            comment_house.save()
            return redirect('house_details',id=id)
        except Exception as e:
            print(e)
            return redirect('house_details',id=id)
    

def dashboard_form_house(request):
    idTourer = ''
    if 'account' in request.session:
        idTourer = request.session['account']
    else:
        idTourer = None
    
    if idTourer == None:
        return render(request,'login/login.html')
    else:
        tourer = Tourer.objects.filter(email=idTourer)
        house = House.objects.all()
        context = {
            'tourer':tourer,
            'house':house
        }
        return render(request,'dashboard/form.html',context)

class IndexView_House(generic.ListView):
    template_name = "dashboard/house/table.html"
    context_object_name = 'house'
    paginate_by = 12
    def get_queryset(self):
        return House.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_House, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_House, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateHouse(CreateView):
    template_name = 'dashboard/house/form.html'
    template_login='login/login.html'
    model = House
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')


   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateHouse, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateHouse, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateHouse, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx
    
 
        
class UpdateHouse(UpdateView):
    template_name = 'dashboard/form.html'
    template_login='login/login.html'
    model = House
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House') #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        # super(UpdateHouse, self).form_valid(form)
        return super(UpdateHouse, self).form_valid(form)


    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateHouse, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateHouse, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class HouseDelete(DeleteView):
    model = House
    success_url = reverse_lazy('IndexView_House')


class IndexView_House_details(generic.ListView):
    template_name = "dashboard/house_details/table.html"
    context_object_name = 'house_details'
    paginate_by = 12
    def get_queryset(self):
        return House_details.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_House_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_House_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateHouse_details(CreateView):
    template_name = 'dashboard/house_details/form.html'
    model = House_details
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')


   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateHouse_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateHouse_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateHouse_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateHouse_details(UpdateView):
    template_name = 'dashboard/house_details/form.html'
    model = House_details
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')


   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateHouse_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateHouse_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateHouse_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class HouseDelete_details(DeleteView):
    model = House_details
    success_url = reverse_lazy('IndexView_House_details')

# city
class IndexView_House_City(generic.ListView):
    template_name = "dashboard/house/city/table.html"
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
            ctx = super(IndexView_House_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_House_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateHouse_City(CreateView):
    template_name = 'dashboard/house/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateHouse_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateHouse_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateHouse_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateHouse_City(UpdateView):
    template_name = 'dashboard/house/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateHouse_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateHouse_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateHouse_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class HouseDelete_City(DeleteView):
    model = City
    success_url = reverse_lazy('IndexView_House_City')

def dashboard_home(request):
    return render(request,'dashboard/dashboard.html')