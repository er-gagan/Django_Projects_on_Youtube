from django.shortcuts import render,HttpResponse
from home.models import Register

# Create your views here.
def index(request):
    return render(request,"Register.html")

def submit_form(request):
    if request.method == 'POST':
        First_Name = request.POST['First_Name']
        Middle_Name = request.POST['Middle_Name']
        Last_Name = request.POST['Last_Name']
        Phone_Number = request.POST['Phone_Number']
        College_Name = request.POST['College_Name']
        Home_Address = request.POST['Home_Address']
        Gender = request.POST['Gender']
        Area_prog=request.POST.get('Programming','off')
        Area_sign=request.POST.get('Singing','off')
        Area_Danc=request.POST.get('Dancing','off')
        Area_Stud=request.POST.get('Studying','off')
        Area_Play=request.POST.get('Playing','off')
        AOI=[]
        if Area_prog == "Programming":
            AOI.append(Area_prog)
        if Area_sign == "Singing":
            AOI.append(Area_sign)
        if Area_Danc == "Dancing":
            AOI.append(Area_Danc)
        if Area_Stud == "Studying":
            AOI.append(Area_Stud)
        if Area_Play == "Playing":
            AOI.append(Area_Play)
        Register(First_Name=First_Name,Middle_Name=Middle_Name,Last_Name=Last_Name,Phone_Number=Phone_Number,College_Name=College_Name,Home_Address=Home_Address,Gender=Gender,Area_Of_Intrest=AOI).save()
        msg="Form Submitted Successfully"
        return render(request,"Register.html",{'msg':msg})
    else:
        return HttpResponse("404 - Not Found")