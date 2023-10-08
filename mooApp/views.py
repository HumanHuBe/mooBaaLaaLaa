from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from django.contrib.auth.decorators import login_required
from .functions import addCode, sentMsg


# Create your views here.
def home(request):
    return render(request, 'mooApp/home.html')

def signupUser(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            pf = ProfileForm()
            return render(request, 'mooApp/signup.html', {'pf' : pf, 'cf' : UserCreationForm})
    elif request.method == 'POST':
        cf = UserCreationForm(request.POST)
        pf = ProfileForm(request.POST)
        if cf.is_valid() and pf.is_valid():
            just_saved_user = cf.save()
            pf = pf.save(commit=False)
            pf.user = just_saved_user
            pf.save()
            login(request, just_saved_user)
        else:
            return render(request, 'mooApp/signup.html', {'pf' : pf, 'cf' : cf})
        return redirect('home')
    else:
        return 'Forbidden'


def loginUser(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'mooApp/login.html', {'af' : AuthenticationForm})
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'mooApp/login.html', {'af' : AuthenticationForm, 'error':'Username and password did not match, please retry!'})
        else:
            login(request, user)
            if request.POST['nextView'] == "":
                return redirect('home')
            else:
                return redirect(request.POST['nextView'])
        



def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return HttpResponse("<h1>FORBIDDEN: YOU CAN NOT LOGOUT LIKE THIS, LOGOUT THROUGH PROPER CHANNEL.</h1>")

    

@login_required
def verification(request):
    x = get_object_or_404(Profile, user=request.user)
    if x.verified:
       return redirect('home')
    else:
        if request.method == 'GET':
            addCode(x)
            sentMsg(x)
            return render(request, 'mooApp/verification.html')
        elif request.method == 'POST':
            if request.POST['otp'] == x.code:
                x.verified = True
                x.save()
                return redirect('products')
            else:
                addCode(x)
                print('code changed')
                sentMsg(x)
                return render(request, 'mooApp/verification.html', {'error':'Entered OTP did not match, kindly re-enter the correct OTP'})
        else:
            return HttpResponse("Forbidden")
        

def products(request):
    x = get_object_or_404(Profile, user=request.user)
    if x.verified:
        return render(request, 'mooApp/products.html')
    else:
        return redirect('verification')