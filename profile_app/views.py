from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render (request,'index.html')

#view profile
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile_app/profile.html', {'profile': profile})

#update profile