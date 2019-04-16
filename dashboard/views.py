from django.shortcuts import render,redirect
from driver.database import mongo_test
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request):
    if mongo_test():
        if request.COOKIES.get('SessionAuth'):
            return render(request,'dashboard.html')
        else:
            return redirect('/')
    else:
        return render(request,'db_error.html')