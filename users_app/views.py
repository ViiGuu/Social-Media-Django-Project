from django.shortcuts import render
from users_app.forms import UserRegistrationForm
from django.contrib.auth.models import User
from main.models import UserInfo

# Create your views here.
def register(request):
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

    return render(request, 'test_registration_form.html', {
        'user_reg_form' : user_reg_form, 
        'registered' : registered})