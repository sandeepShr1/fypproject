# I have created this fie.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
import joblib


# create yours views here


def index(request):

    return render(request, "index.html")



def result(request):
    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['Bedroom'])
    lis.append(request.GET['Bathroom'])
    lis.append(request.GET['Floor'])
    lis.append(request.GET['Area'])
    lis.append(request.GET['City'])
    lis.append(request.GET['Parking'])
    lis.append(request.GET['Frontyard'])
    lis.append(request.GET['RoadType'])

    print(lis)

    ans = cls.predict([lis])

    return render(request, "result.html", {'ans': ans})


def about_us(request):
    return render(request, "about.html")






