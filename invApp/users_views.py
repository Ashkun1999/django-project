from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def register_view(request):
    """
    Handle user registration
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            # Log the user in immediately after registration
            login(request, user)
            return redirect('product_list')  # Redirect to product list after registration
    else:
        form = UserCreationForm()
    
    return render(request, 'invApp/register.html', {'form': form})


def login_view(request):
    """
    Handle user login
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # AuthenticationForm.get_user() returns the authenticated user 
            # after the form validation is successful
            user = form.get_user()
            login(request, user)
            messages.success(request, f'You are now logged in as {user.username}')
            # Redirect to a success page
            return redirect('product_list')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'invApp/login.html', context)


def logout_view(request):
    """
    Handle user logout
    """
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')  # Redirect to login page after logout
