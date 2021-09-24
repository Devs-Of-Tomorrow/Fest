from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View
import random
from management.models.participants import SignInUser
from django.http import HttpResponseNotAllowed


class SignIn(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        genotpp = request.POST.get('genotp')
        gender = request.POST.get('gender')
        
        if genotpp:
            otp = str(random.randint(1000,9999))
            request.session['session_otp'] = otp
            # import smtplib
            # ser = smtplib.SMTP("smtp.gmail.com", 587)
            # ser.starttls()
            # ser.login("amir.visualizeindia@gmail.com","pass")
            # msg = otp
            # ser.sendmail("amir.visualizeindia@gmail.com", "amir.visualizeindia@gmail.com", msg)
            # print("mail sent sucessfully")
            # ser.quit()

        
        print('genotpsdsds', genotpp, request.session.get('session_otp'))

        hashpassword = None
        
        
        error_message = None
        signinuser = SignInUser(first_name=first_name,
                                last_name=last_name,
                                gender=gender,
                                email=email,
                                phone=phone,
                                password=password
                                )

        error_message = self.validatesignin(signinuser)

        if not error_message:
            
            # signinuser.password = make_password(signinuser.password)

            # signinuser.register()
            
            request.session['tryfirst_name'] = first_name
            request.session['trylast_name'] = last_name
            request.session['tryemail'] = email 
            request.session['tryphone'] = phone
            request.session['trypassword'] = password
            return redirect("genotp")

        else:
            data = {
                'error_message': error_message
            }
       
        return render(request, 'signup.html', data)

    def validatesignin(self, signinuser):
        error_message = None
        if signinuser.IsExists():
            error_message = "email alrady exists"
        return error_message

def genotp(request):

    otp = request.session.get('session_otp')
    error_message = SignInUser.objects.filter(email=request.session.get('tryemail')).first()
    
    if error_message:
        return HttpResponseNotAllowed('<h1>Not Allowed</h1>')
    if not request.session.get('tryemail'):
        return HttpResponseNotAllowed('<h1>Not Allowed</h1>')

    if request.method == 'POST':
        first_name = request.session.get('tryfirst_name')
        last_name = request.session.get('trylast_name')
        email = request.session.get('tryemail')
        phone = request.session.get('tryphone')
        password = request.session.get('trypassword')
        form_otp = request.POST.get('form_otp')
        
        signinuser = SignInUser(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone=phone,
                                password=password
                                )

        if otp==form_otp:
            signinuser.password = make_password(signinuser.password)
            signinuser.register()
            user = SignInUser.objects.filter(email=email).first()
            request.session['user_id'] = user.id
            request.session['email'] = email
            return redirect('home')  

        else:
            print("reetryy")

        print('ffffoootototop',form_otp)

    print('oootototop', error_message, otp)
    return render(request, 'otp.html')
