from django.shortcuts import render,HttpResponse,get_object_or_404, redirect,HttpResponseRedirect
from .models import Tourer
from django.views.generic.edit import CreateView
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
            email_login = Tourer.objects.get(email=email)
            login = 1
        except Exception as e:
            login = 0

        if login == 1:
            if email_login.password == password:
                request.session['account'] = email_login.email
                return redirect(request.POST['next'])
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

def error(request):
    return render(request,'error/error.html')