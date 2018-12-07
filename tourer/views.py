from django.shortcuts import render,HttpResponse,get_object_or_404, redirect,HttpResponseRedirect
from .models import Tourer, Account
from django.views.generic.edit import CreateView
from passlib.hash import sha256_crypt
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic

# from .forms import Tourer_form
# Create your views here.
def login(request):
    next_page = request.GET['next']
    context = {
        'next':next_page
    }
    return render(request,'login/login.html',context)

def logout(request):  
    try:
        request.session.pop('account')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    except Exception as e:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
        

def login_form(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        login = 0
        email_login = ''
        password_email = ''
        error = ''
        try:
            email_login = Account.objects.get(email=email)
            login = 1
        except Exception as e:
            login = 0

        if login == 1:
            if sha256_crypt.verify(password,email_login.password) == True:
                try:
                    request.session['account'] = email_login.email
                    return redirect(request.POST['next'])
                except Exception as e:         
                    return redirect('home')
            else:
                error = 'Sai Mật Khẩu'
                context = {
                    'error' : error
                }
                return render(request,'login/login.html',context)
        else:
            error = 'Tên Đăng Nhập Không Đúng'
            context = {
                    'error' : error
            }
            return render(request,'login/login.html',context)

class Register(CreateView):
    template_name = 'login/register.html'
    model = Tourer
    fields = '__all__'

    
    #urls name
    def form_valid(self, form):
        # Instead of return this HttpResponseRedirect, return an 
        #  new rendered page
       
        return  super(Register, self).form_valid(form)
        # return logout(self.request)

def register_main(request):
    return render(request,'login/register.html')

def form_signup(request):
    email = request.POST['email']
    name = request.POST['name']
    password  = request.POST['password']
    password = sha256_crypt.encrypt(password)
    if request.method == 'POST' :
        try:
            tourer = Account.objects.create(email=email,name=name,password=password,question='Null',author='account')
            context = {
                'message' : 'message'
            }
            return render(request,'login/login.html',context)
        except Exception as e:
            return render(request,'error/index.html',{
                'error':'email already exists, please enter another email'
            })
    else:
        context = {
             'message' : 'message'
        }
        return render(request,'login/register.html',context)

def error(request):
    return render(request,'error/error.html')

