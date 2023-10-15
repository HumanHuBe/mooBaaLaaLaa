from django.shortcuts import redirect
def home(request):
    return redirect('home', permanent=True)