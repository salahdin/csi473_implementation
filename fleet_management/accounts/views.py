from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #remember to log the user in
            return redirect('accounts:signup')
        else:
            form = UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})