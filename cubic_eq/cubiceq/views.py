from django.shortcuts import render
from django.http import HttpResponse
from .forms import CubiceqForm
import sympy as sp
from sympy import Symbol, simplify
import numpy as np 

def index(request):
    params = {
        'title':'Cubic', 
        'forms': CubiceqForm(),
        'solution': 'ここに解が表示されます'
    }
    if (request.method == 'POST'):

        x=Symbol('x')
        a = int(request.POST['val1'])
        b = int(request.POST['val2']) 
        c = int(request.POST['val3'])
        d = int(request.POST['val4'])
        Sol3=sp.solve (a*x**3+b*x**2+c*x+d, x)
        
        params['solution'] = sp.latex(Sol3)
        params['forms'] = CubiceqForm(request.POST)

    return render(request, 'cubiceq/index.html', params)