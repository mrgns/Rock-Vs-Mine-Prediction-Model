import re
from django.shortcuts import render, HttpResponse

import pandas as pd
import numpy as np
from . import action
import joblib

#reloadmodel = joblib.load('models/predictionModel.pkl.pkl')

def index(request):
    #return HttpResponse("This is Index")
    return render(request, 'index.html')

def getPredection(d):
    return action.getData(d)  


def data(request):
    if request.method == "POST":
        #print(request.POST.dict())
        file = request.POST.get('file')
        str = 'E:\\'+file
        df = pd.read_csv(str)
        d = list(df)
        #print(d)
        text = getPredection(d)
        if text == "R":
            return render(request,'stone.html')
        else:
            return render(request, 'mine.html')
