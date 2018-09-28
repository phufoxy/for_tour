from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Book_Tour,Restaurant_tour,Place_tour,Vehicle_tour,House_tour,Book_Tour_Details,Album_Tour
from tourer.models import Tourer
from datetime import datetime

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
    account = Tourer.objects.get(email=idempresa)
    book_Tour = Book_Tour.objects.filter(tourer=account).order_by('-id')
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
    place_tour = Place_tour.objects.filter(book=book_Tour)
    count_place = Place_tour.objects.filter(book=book_Tour).count()
    context = {
        'idempresa':idempresa,
        'book_Tour':book_Tour,
        'place_tour':place_tour,
        'count_place':count_place
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
            account_details = Tourer.objects.get(email=idempresa)
            book_Tour = Book_Tour(name_book=name_book,date_book=datetime.now(),date_start=date_book,tourer=account_details)
            book_Tour.save()
            return redirect('book_details')
        except Exception as e:
            print(e)
            return redirect('book')
