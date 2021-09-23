from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View

from management.models.participants import SignInUser


class LogIn(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = SignInUser.get_signinuser_by_email(email)
        print('eeeeeeeeeemmmmmm', email)

        if user:
            flag = check_password(password, user.password)
            print(user, user.email, user.first_name)
            if flag:
                request.session['email'] = user.email
                request.session['user_id'] = user.id
                request.session['user_profile_url'] = str(user.profile_image)
                print('naaaaaaa', user.first_name)

                return redirect('home')
            else:
                error_message = 'Email or Password invalid !!!'
        else:
            error_message = 'Email or Password invalid !!!'
            print('loggggggggggg')

        return render(request, 'login.html', {'error_message': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')
