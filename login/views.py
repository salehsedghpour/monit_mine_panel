from django.shortcuts import render
from driver.database import mongo_test
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from base64 import b64encode
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
def login(request):
    if mongo_test():
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = LoginForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                global username
                global userpass
                username = request.POST['username']
                userpass = request.POST['password']
                user = authenticate(request, username=username, password=userpass)
                combined = username + ':' + userpass

                if user is not None:
                    #login(request)
                    response = HttpResponseRedirect('/monitoring/')
                    response.set_cookie("SessionAuth", b64encode(bytes(combined, encoding='utf-8')).decode("ascii"),
                                        max_age=3600)
                    return response
                else:
                    value = True

            # if a GET (or any other method) we'll create a blank form
        else:

            form = LoginForm()
            value = False

        return render(request, 'login.html', {'form': form, 'invalid': value, })
    else:
        return render(request=request, template_name='db_error.html')


def logout_view(request):
    logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie('SessionAuth')
    return response
