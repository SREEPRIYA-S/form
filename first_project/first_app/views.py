from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
import joblib
import numpy as np


def index(request) :
    return render(request,'index.html')
def about(request) :
    return render(request,'about.html')
def contact(request) :
    return render(request,'contact.html')
def predictor(request) :
    return render(request,'predictor.html')


def result(request) :

    cls = joblib.load('finalized_model.sav')
    lis = []
    lis.append(request.GET['age'])
    lis.append(request.GET['sex'])
    lis.append(request.GET['cp'])
    lis.append(request.GET['trestbps'])
    lis.append(request.GET['chol'])
    lis.append(request.GET['fbs'])
    lis.append(request.GET['restecg'])
    lis.append(request.GET['thalach'])
    lis.append(request.GET['exang'])
    lis.append(request.GET['oldpeak'])
    lis.append(request.GET['slope'])
    lis.append(request.GET['ca'])
    lis.append(request.GET['thal'])
    print(lis)
    lis = [float(x) for x in lis]  # Convert each element in the list to integer
    lis = np.array(lis).astype(float)  # Convert the list to a numpy array of float type

    ans = cls.predict([lis])
    if ans == 0:
        ans = "You are healthy"
    else:
        ans = "You have been predicted to have a heart disease. We recommend consulting a doctor or taking a medical check-up for further evaluation and advice."
    return render(request, "result.html", {'ans': ans})