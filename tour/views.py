from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from .models import Tour,PlaceTour
from tourer.models import Tourer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum,Count
from django.db.models import F

# Create your views here.
class ListTour(generic.ListView):
    template_name = "dashboard/tour/tour/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return Tour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListTour, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddTour(CreateView):
    template_name = 'dashboard/tour/tour/form.html'
    model = Tour
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddTour, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddTour, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdateTour(UpdateView):
    template_name = 'dashboard/tour/tour/form.html'
    model = Tour
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdateTour, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdateTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdateTour, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeleteTour(DeleteView):
    model = Tour
    success_url = reverse_lazy('ListTour')


class ListPlaceTour(generic.ListView):
    template_name = "dashboard/tour/place_tour/table.html"
    context_object_name = 'context'
    paginate_by = 12
    def get_queryset(self):
        return PlaceTour.objects.all().order_by("-id")

    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(ListPlaceTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(ListPlaceTour, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class AddPlaceTour(CreateView):
    template_name = 'dashboard/tour/place_tour/form.html'
    model = PlaceTour
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(AddPlaceTour, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(AddPlaceTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(AddPlaceTour, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class UpdatePlaceTour(UpdateView):
    template_name = 'dashboard/tour/place_tour/form.html'
    model = PlaceTour
    fields = '__all__'
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
        return super(UpdatePlaceTour, self).form_valid(form)

    
    def get_context_data(self, **kwargs):
        if 'account' in self.request.session:
            idTourer = self.request.session['account']
        else:
            idTourer = None
        if idTourer == None:
            ctx = super(UpdatePlaceTour, self).get_context_data(**kwargs)
            tourer=None
            ctx['tourer'] = tourer
            return ctx
        else:
            ctx = super(UpdatePlaceTour, self).get_context_data(**kwargs)
            tourer = Tourer.objects.filter(email=idTourer)
            ctx['tourer'] = tourer
            return ctx

class DeletePlaceTour(DeleteView):
    model = PlaceTour
    success_url = reverse_lazy('ListPlaceTour')

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
# filter
@register.filter
def in_place(tour):
    return PlaceTour.objects.filter(tour=tour).aggregate(Sum('price'))


# list tour
def list_tour(request):
    tour = Tour.objects.annotate(sum_price = Sum(F('price')*F('person'))).order_by('-id')
    idempresa= ''
    if 'account' in request.session:
        idempresa = request.session['account']
    else:
        idempresa=None
        
    page = request.GET.get('page', 1)

    paginator = Paginator(tour, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = { 
        'idempresa':idempresa,
        'context':users,
    }
    return render(request,'home/tour/tour.html',context)

def tour_details(request,id):
    tour = Tour.objects.get(id=id)
    placeTour = PlaceTour.objects.filter(tour=tour)
    context = {
        'context':placeTour
    }
    return render(request,'home/tour/tour_details.html',context)