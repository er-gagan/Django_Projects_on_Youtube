from django.shortcuts import render
from Myapp.models import CompanyClass,EmployeeClass
# Create your views here.
def Home(request):
    return render(request,"Home.html")

def Company(request):
    return render(request,"Company.html")

def Employee(request):
    return render(request,"Employee.html")

def SearchingCom(request):
    return render(request,"SearchingCom.html")

def SearchingEmp(request):
    return render(request,"SearchingEmp.html")

def EmployeeData(request):
    Employee_ID = request.GET['Employee_ID']
    Name = request.GET['Name']
    Age = request.GET['Age']
    Phone = request.GET['Phone']
    City = request.GET['City']
    EmployeeClass(Employee_ID=Employee_ID,Name=Name,Age=Age,Phone=Phone,City=City).save()
    msg="Your Record Stored Successfully"
    return render(request,"Employee.html",{'msg':msg})

def CompanyData(request):
    Job_Profile_ID = request.GET['Job_Profile_ID']
    JobProfile = request.GET['JobProfile']
    Salary = request.GET['Salary']
    Employee_ID = request.GET['Employee_ID']
    CompanyClass(Job_Profile_ID=Job_Profile_ID,JobProfile=JobProfile,Salary=Salary,Employee_ID=Employee_ID).save()
    msg="Your Record Stored Successfully"
    return render(request,"Company.html",{'msg':msg})

def EmpData(request):
    data = request.GET['data']
    return render(request,"SearchingEmp.html")

def ComData(request):
    data = request.GET['data']
    return render(request,"SearchingCom.html")

def ViewEmpData(request):
    EmpData = EmployeeClass.objects.all()
    count = EmployeeClass.objects.count()
    # Rec = EmployeeClass.objects.all()[0:5:1] # [start:stop:step]
    Rec = EmployeeClass.objects.all()[::-1] # print all data in reverse order
    return render(request,"ViewEmpData.html",{'EmpData':EmpData,'count':count,'Rec':Rec})