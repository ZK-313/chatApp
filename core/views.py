from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

#def frontpage(request):
#    if request.user.is_authenticated:
#        return redirect('chat')
#    return redirect('core/login.html')

def front_test(request):
    if request.user.is_authenticated:
        return redirect('chat')
    return redirect('/login')

def chat(request):
    return render(request, 'core/chat.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('chat')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

# Create your views here.
