from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import House,House_details,Comment_house
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
    house_items = House.objects.order_by('-id')
    city = House.objects.values('city').distinct()
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
        'idempresa':idempresa,
        'city':city

    }
    return render(request,'home/hotels.html',context)

def form_search(request):
    if request.method == "POST":
        name = request.POST['city']
        if name == "all":
            return redirect('/house')
        else:
            return redirect('/house/search/'+name)

def house_search(request,name):
    house_items = House.objects.filter(city=name)
    city = House.objects.values('city').distinct()
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
        'idempresa':idempresa,
        'city':city
    }
    return render(request,'home/hotels.html',context)

def house_details(request,id):
    try:
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

        if idempresa == None:
            return redirect('/login/?next='+ request.path)
        else:
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
    except House.DoesNotExist as e:
        return render(request,'error/index.html',{
            'error':'wrong routing path'
        })
    

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

class ListHouse(generic.ListView):
    template_name = "dashboard/house/table.html"
    context_object_name = 'house'
    paginate_by = 8
    def get_queryset(self):
        return House.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListHouse, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListHouse, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddHouse(CreateView):
    template_name = 'dashboard/house/form.html'
    template_login='login/login.html'
    model = House
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')

    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddHouse, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddHouse, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddHouse, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx
    
 
        
class UpdateHouse(UpdateView):
    template_name = 'dashboard/house/form.html'
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

class DeleteHouse(DeleteView):
    model = House
    success_url = reverse_lazy('IndexView_House')


class ListHouseDetails(generic.ListView):
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
            ctx = super(ListHouseDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListHouseDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddHouseDetails(CreateView):
    template_name = 'dashboard/house_details/form.html'
    model = House_details
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')
   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddHouseDetails, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddHouseDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddHouseDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateHouseDetails(UpdateView):
    template_name = 'dashboard/house_details/form.html'
    model = House_details
    fields = '__all__'
    # success_url = reverse_lazy('IndexView_House')
   
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateHouseDetails, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateHouseDetails, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateHouseDetails, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteHouseDetails(DeleteView):
    model = House_details
    success_url = reverse_lazy('IndexView_House_details')


def dashboard_home(request):
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None

    if idempresa == None:
        return redirect('/login/?next='+ request.path)
    else:
        account = Tourer.objects.get(email=idempresa)
        author_account = account.author
        if author_account == "admin" :
            return render(request,'dashboard/home/home.html')
        else :
            return render(request,'error/index.html',{
                'error':'You are not an administrator'
            })

def error_page(request):
    return render(request,'error/index.html')