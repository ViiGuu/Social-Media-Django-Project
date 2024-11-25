from django.shortcuts import render
from users_app.forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from main.models import UserInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def user_register(request):
    registered = False

    if request.method == 'POST':
        user_reg_form = UserRegistrationForm(data=request.POST)

        if user_reg_form.is_valid():
            user = User.objects.create_user(
                username=user_reg_form.cleaned_data['username'], 
                password=user_reg_form.cleaned_data['password'])
            
            #links user to a UserInfo model (so they can upload profile pics etc.)
            UserInfo.objects.create(user=user)
            registered = True
        else:
            print(user_reg_form.errors)
        
    else:
        user_reg_form = UserRegistrationForm()

    return render(request, 'test_registration_form.html', { #placeholder html for testing
        'user_reg_form' : user_reg_form, 
        'registered' : registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'test_login_success.html') #placeholder html for testing, remove later and return HttpResponseRedirect below instead
                # return HttpResponseRedirect(reverse('')) #redirect to home/index page once it's implemented
            else:
                return HttpResponse('User not active')
            
        else:
            print(f"Login failed for user: {username}")
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'test_login.html') #placeholder html for testing