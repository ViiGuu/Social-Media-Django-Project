from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from profile_app.models import Profile

def index(request):
    return render (request,'index.html')

#view profile
@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile_app/profile.html', {'profile': profile})

#update profile