from django.shortcuts import render,HttpResponse,get_object_or_404, redirect
from .models import Tourer
from django.views.generic.edit import CreateView
# from .forms import Tourer_form
# Create your views here.
def login(request):
    return render(request,'login/login.html')

def logout(request):  
    try:
        request.session.pop('account')
        return redirect('login')
    except Exception as e:
        return redirect('login')
        

def login_form(request):
    email = request.GET['email']
    password = request.GET['password']
    login = 0
    email_login = ''
    password_email = ''
    error = ''
    try:
        email_login = Tourer.objects.get(email=email)
        print(email_login)
        login = 1
    except Exception as e:
        login = 0

    if login == 1:
        if email_login.password == password:
            request.session['account'] = email_login.email
            return redirect('house')
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
        super(Register, self).form_valid(form)
        return logout(self.request)

def error(request):
    return render(request,'error/error.html')