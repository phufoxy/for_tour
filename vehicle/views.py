from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Type_vehicle,City,Vehicle,Vehicle_details,Car_details,Comment_Vehicle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from tourer.models import Tourer
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from book.models import Book_Tour,Vehicle_tour

# Create your views here.
def index(request):
    vehicle = Vehicle.objects.select_related('location').order_by('-id')
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    page = request.GET.get('page', 1)

    paginator = Paginator(vehicle, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'idempresa': idempresa,
        'context': users
    }
    return render(request,'home/vehicle/vehicle.html',context)

def vehicle_details(request,id):
    vehicle = Vehicle.objects.get(pk=id)
    vehicle.review = vehicle.review + 1
    vehicle.save()
    # account
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    if idempresa == None:
        return redirect('login')
    else:
        vehicle_details = Vehicle_details.objects.filter(vehicle=id)
        # page = request.GET.get('page', 1)

        # paginator = Paginator(vehicle_details, 10)
        # try:
        #     users = paginator.page(page)
        # except PageNotAnInteger:
        #     users = paginator.page(1)
        # except EmptyPage:
        #     users = paginator.page(paginator.num_pages)
        # context
        account = Tourer.objects.get(email=idempresa)
        book_Tour = Book_Tour.objects.filter(tourer=account).order_by('-id')
        context = {
            'idempresa': idempresa,
            'context':vehicle_details,
            'id_car':id,
            'vehicle':vehicle,
            'book_Tour':book_Tour
        }
        return render(request,'home/vehicle/vehicle_details.html',context)

def car_details(request,id,id_car):
    car_details = Car_details.objects.filter(car=id_car)
    vehicle_details = Vehicle_details.objects.get(id=id)
    # account
    idempresa = ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa = None

    tourer = Tourer.objects.filter(email=idempresa)
    # eatings = Eating.objects.filter(restaurant=id)
    sum_commnet = Comment_Vehicle.objects.filter(vehicle=id).count()
    comment = Comment_Vehicle.objects.filter(
        vehicle=id).order_by('-date')
    # context
    context = {
        'idempresa': idempresa,
        'tourer': tourer,
        'sum_commnet': sum_commnet,
        'comment': comment,
        'car_details':car_details,
        'vehicle_details':vehicle_details,
    }
    return render(request,'home/vehicle/car_details.html',context)

def create_vehicle_tour(request,id):
    vehicle_details = Vehicle_details.objects.get(pk=id)
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
            vehicle_tour = Vehicle_tour(book=book_Tour,vehicle_details=vehicle_details,account=account_details,date_book=datetime.now(),date_to=date_to)
            vehicle_tour.save()
            return redirect('vehicle_details',id=id)
        except Exception as e:
            print(e)
            return redirect('vehicle_details',id=id)

def create_comment_vehicle(request,id):
    vehicle = Vehicle_details.objects.get(pk=id)
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
            comment_place = Comment_Vehicle(vehicle=vehicle,commnet=commnet_items,date=datetime.now(),account=account_details)
            comment_place.save()
            return redirect('vehicle_details',id=id)
        except Exception as e:
            print(e)
            return redirect('vehicle_details',id=id)

# city
class IndexView_Vehicle_City(generic.ListView):
    template_name = "dashboard/vehicle/city/table.html"
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
            ctx = super(IndexView_Vehicle_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Vehicle_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateVehicle_City(CreateView):
    template_name = 'dashboard/vehicle/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateVehicle_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateVehicle_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateVehicle_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateVehicle_City(UpdateView):
    template_name = 'dashboard/vehicle/city/form.html'
    model = City
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateVehicle_City, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateVehicle_City, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateVehicle_City, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class VehicleDelete_City(DeleteView):
    model = City
    success_url = reverse_lazy('IndexView_Vehicle_City')

# Type_vehicle
class IndexView_Type_vehicle(generic.ListView):
    template_name = "dashboard/vehicle/type_vehicle/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Type_vehicle.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_Type_vehicle, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_Type_vehicle, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class CreateType_vehicle(CreateView):
    template_name = 'dashboard/vehicle/type_vehicle/form.html'
    model = Type_vehicle
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateType_vehicle, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(CreateType_vehicle, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(CreateType_vehicle, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateType_vehicle(UpdateView):
    template_name = 'dashboard/vehicle/type_vehicle/form.html'
    model = Type_vehicle
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateType_vehicle, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateType_vehicle, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateType_vehicle, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Type_vehicleDelete(DeleteView):
    model = Type_vehicle
    success_url = reverse_lazy('IndexView_Type_vehicle')

# vehicle
class IndexView_vehicle(generic.ListView):
    template_name = "dashboard/vehicle/vehicle/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Vehicle.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_vehicle, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_vehicle, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Create_Vehicle(CreateView):
    template_name = 'dashboard/vehicle/vehicle/form.html'
    model = Vehicle
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(CreateType_vehicle, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(Create_Vehicle, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(Create_Vehicle, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateVehicle(UpdateView):
    template_name = 'dashboard/vehicle/vehicle/form.html'
    model = Vehicle
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateVehicle, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateVehicle, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateVehicle, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('IndexView_vehicle')

# vehicle_details
class IndexView_vehicle_details(generic.ListView):
    template_name = "dashboard/vehicle/vehicle_details/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Vehicle_details.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_vehicle_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_vehicle_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Create_vehicle_details(CreateView):
    template_name = 'dashboard/vehicle/vehicle_details/form.html'
    model = Vehicle_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(Create_vehicle_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(Create_vehicle_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(Create_vehicle_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Updatevehicle_details(UpdateView):
    template_name = 'dashboard/vehicle/vehicle_details/form.html'
    model = Vehicle_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(Updatevehicle_details, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(Updatevehicle_details, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(Updatevehicle_details, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Vehicle_detailsDelete(DeleteView):
    model = Vehicle_details
    success_url = reverse_lazy('IndexView_vehicle_details')

# Car_details
class IndexView_car(generic.ListView):
    template_name = "dashboard/vehicle/car_details/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Car_details.objects.all()

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(IndexView_car, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(IndexView_car, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Create_Car(CreateView):
    template_name = 'dashboard/vehicle/car_details/form.html'
    model = Car_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(Create_Car, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(Create_Car, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(Create_Car, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateCar(UpdateView):
    template_name = 'dashboard/vehicle/car_details/form.html'
    model = Car_details
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateCar, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateCar, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateCar, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class Vehicle_detailsDelete(DeleteView):
    model = Car_details
    success_url = reverse_lazy('IndexView_car')