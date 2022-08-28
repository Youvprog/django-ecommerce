from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()



def sign_up_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, 
                                            email=email, 
                                            first_name=first_name, 
                                            last_name=last_name, 
                                            password=password1)
            login(request, user)
            return redirect('products-list')

    return render(request,'accounts/signup.html')




def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user:
            login(request,user)
            return redirect('products-list')

    return render(request, 'accounts/login.html')



