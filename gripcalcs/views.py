from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.
def index(request):
    return render(request, "input.html")

def torquetoforce(request):
    return render(request, "torque.html")

def torquetoforce_calc(request):
    forceStr = request.POST.get("force")
    leadStr = request.POST.get("lead")
    efficiencyStr = request.POST.get("efficiency")
    print(forceStr, leadStr, efficiencyStr )
    if is_number(forceStr) and is_number(leadStr) and is_number(efficiencyStr):

        force = float(forceStr)
        lead = float(leadStr)
        efficiency = float(efficiencyStr)
        torque = force * lead / (2000 * math.pi * efficiency )

        return render(request, "torque.html", {"torque" : torque})
    else:
        torque = "Only digits are allowed"
        return render(request, "torque.html", {"torque": torque})

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def verticalmoment_load(request):
    return render(request, "vertical.html")

def verticalmoment(request):
    massStr = request.POST.get("partmass")
    supmassStr = request.POST.get("supportmass")
    gravityStr = request.POST.get("gravity")
    accelerationStr = request.POST.get("acceleration")
    l1Str = request.POST.get("l1")
    l2Str = request.POST.get("l2")
    h1Str = request.POST.get("h1")
    h2Str = request.POST.get("h2")
    safetyStr = request.POST.get("safety")
    print(massStr, supmassStr, gravityStr, accelerationStr, l1Str, l2Str, h1Str, h2Str,safetyStr)
    if is_number(massStr) and is_number(accelerationStr) and is_number(gravityStr) and is_number(l1Str) and is_number(l2Str) and is_number(h1Str) and is_number(h2Str) and is_number(safetyStr):

        mass = float(massStr)
        supmass = float(supmassStr)
        acceleration = float(accelerationStr)
        gravity = float(gravityStr)
        l1 = float(l1Str)
        l2 = float(l2Str)
        h2 = float(h2Str)
        h1 = float(h1Str)
        safety = float(safetyStr)
        my = safety * (mass * (gravity + acceleration) * l1/1000 + supmass *(gravity + acceleration) * l2 / 1000)
        mz = safety * (mass * (gravity + acceleration) * h1/1000 + supmass *(gravity + acceleration) * h2 / 1000)

        return render(request, "vertical.html", {"mymoment" : my, "mzmoment": mz})
    else:
        mz = "Only digits are allowed"
        my = "Only digits are allowed"
        return render(request, "vertical.html", {"result": res})

def addition(request):

    massStr = request.POST.get("mass")
    accelerationStr = request.POST.get("acceleration")
    gravityStr = request.POST.get("gravity")
    coeffStr = request.POST.get("coeff")
    safetyStr = request.POST.get("safety")
    if is_number(massStr) and is_number(accelerationStr) and is_number(gravityStr) and is_number(coeffStr) and is_number(safetyStr):

        mass = float(massStr)
        acceleration = float(accelerationStr)
        gravity = float(gravityStr)
        coeff = float(coeffStr)
        safety = float(safetyStr)
        gripforce = safety * (mass * (gravity + acceleration)) / coeff

        return render(request, "input.html", {"result": gripforce})
    else:
        res = "Only digits are allowed"
        return render(request, "input.html", {"result": res})

