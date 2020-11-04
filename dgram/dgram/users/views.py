from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SingUpForm

def main(request):
    if request.method == "GET":
        return render(request, 'users/main.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            return render(request, 'users/main.html')

def signup(request):
    if request.method == "GET":
        form = SingUpForm()

        return render(request, 'users/signup.html', {'form': form})
    
    elif request.method == "POST":
        form = SingUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            # 유효한 데이터는 cleaned 에 저장된다
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:index'))
            
        return render(request, 'users/main.html')            

