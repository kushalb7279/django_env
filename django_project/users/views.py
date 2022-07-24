from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required   #used to give access to a page only after login
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.
def register(request):
    if request.method == 'POST':   #type of http response which sends data back to the server
        form = UserRegisterForm(request.POST)   #request.POST used to populate the form instead of displaying empty values
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')    #cleaned_data is a dictionary
            messages.success(request, f'Account created for {username}! You can now login')  #this sends a flash message
            return redirect('login')
    else:
        form = UserRegisterForm()   #blank form
    return render(request, 'users/register.html', {'form': form})


# @login_required         #from libary imported above
# def profile(request):
#     return render(request, 'users/profile.html')



@login_required         #from libary imported above
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',context)
