from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# def hoods(request):
#     all_hoods = NeighbourHood.objects.all()
#     all_hoods = all_hoods[::-1]
#     params = {
#         'all_hoods': all_hoods,
#     }
#     return render(request, 'all_hoods.html', params)