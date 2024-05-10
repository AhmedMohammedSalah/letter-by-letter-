from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import reverse
from .models import CustomUser  # Import your custom user modelfrom .
from .forms import SignupForm
import random
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

import string  # Import string module for generating random characters
def login_view(request):
    if request.method == 'POST':
        nid = request.POST.get('nid')
        # Assuming CustomUser model with nid field
        user = authenticate(request, nid=nid)
        # {null , null}
        # 
        
        if user is not None:
            login(request, user)
            return redirect('base')   # Redirect to the base.html or your desired success page
        else:
            # Handle invalid NID
            signup_url = f'/accounts/signup/?nid={nid}'  # Construct signup URL with nid parameter
            return redirect(signup_url)
            # form = SignupForm(initial={'nid': nid}) 
            # return render(request, 'registration/signup.html', {"form": form})
    else:
        return render(request, 'registration/login.html')



def signup_view(request):
    if request.method == 'POST':
        # Get nid from the query parameters
        nid = request.GET.get('nid')

        # Check if a user with the given nid already exists
        if CustomUser.objects.filter(nid=nid).exists():
            return render(request, 'registration/signup.html', {'error': 'الرقم القومي مستخدم بالفعل'})

        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            # Extract cleaned data from the form
            fname = form.cleaned_data['fname']
            image = form.cleaned_data['image']
            age = form.cleaned_data['age']
            # nid Fake username and password
            # Generate a unique username (ensure it doesn't exist already)
            username = str(uuid.uuid4())[:30]
            
            while CustomUser.objects.filter(username=username).exists():
                username = str(uuid.uuid4())[:30]

            # Create a new CustomUser instance
            user = CustomUser.objects.create_user(username=username, password='temp_password', nid=nid, fname=fname, image=image, age=age)

            # Authenticate and log in the user
            user = authenticate(request, username=username, password='temp_password')

            signin_url = f'/accounts/login/?nid={nid}'  # Construct signup URL with nid parameter
            return redirect(signin_url)  # Redirect to success page after login

    else:
        # If not a POST request, retrieve nid from query parameters
        nid = request.GET.get('nid')
        form = SignupForm(initial={'nid': nid})  # Create a new instance of the form

    return render(request, 'registration/signup.html', {'form': form})