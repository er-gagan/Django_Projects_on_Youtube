from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        return render(request, "Bulb_On.html")
    else:
        return render(request, "Bulb_Off.html")