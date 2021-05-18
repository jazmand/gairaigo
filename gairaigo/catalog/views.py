from django.shortcuts import render

import pandas as pd 
import random

# Create your views here.
def generate(request):
    df = pd.read_excel (r'C:\Users\Judi\Desktop\Programming\GitHub Repositories\gairaigo\GairaigoExcel.xlsx')

    x=[]
    for value in  df.iloc[:, 0]:
        x.append(value)
    jp = random.choice(x)
    index = x.index(jp)

    y=[]
    for value in  df.iloc[:, 1]:
        y.append(value)
    eng = y[index]    

    return render(request, "catalog/layout.html", {
        "jp": jp,
        "eng": eng        
    })
