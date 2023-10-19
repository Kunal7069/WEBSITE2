from django.http import HttpResponse
from django.shortcuts import render
from login.models import Student,Faculty,Detail
def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=='POST':
        usertype =request.POST.get('user-type')
        if usertype == 'student':
            username =request.POST.get('username')
            password =request.POST.get('password')
            students=Student.objects.all()
            for x in students:
                if x.username==username and x.password==password:
                    return render(request,"home2.html")
            return HttpResponse("INCORRECT")
        if usertype == 'teacher':
            username =request.POST.get('username')
            password =request.POST.get('password')
            faculty=Faculty.objects.all()
            for x in faculty:
                if x.username==username and x.password==password:
                    students=Detail.objects.all()
                    return render(request,"data.html",{'students':students})
            return HttpResponse("GOEL INTERUPT")
            
def signup(request):
    return render(request,"signup.html")

def signedup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        rollno=request.POST.get('roll_no')
        emailid =request.POST.get('email')
        username =request.POST.get('username')
        password =request.POST.get('password1')
        en=Student(name=name,rollno=rollno,emailid=emailid,username=username,password=password)
        en.save()
        return render(request,"home.html")


def form1(request):
    return render(request,"form1.html")

def form2(request):
    if request.method=='POST':
        date = request.POST.get('date')
        branch = request.POST.get('branch')
        rollno= request.POST.get('rollno')
        studentname = request.POST.get('studentname')
        category= request.POST.get('category')
        fathername= request.POST.get('fathername')
        occuption= request.POST.get('occuption')
        income= request.POST.get('income')
        address= request.POST.get('address')
        localguardianname = request.POST.get('localguardianname')
        localguardianaddress= request.POST.get('localguardianaddress')
        mobilenumberguardian= request.POST.get('mobilenumberguardian')
        mobilenumberself= request.POST.get('mobilenumberself')
        mobilenumberfather= request.POST.get('mobilenumberfather')
        mobilenumbermother= request.POST.get('mobilenumbermother')
        emailself= request.POST.get('emailself')
        emailparent= request.POST.get('emailparent')
        accountnumber= request.POST.get('accountnumber')
        ifsc= request.POST.get('ifsc')
        bank= request.POST.get('bank')
        accountholdername= request.POST.get('accountholdername')
        marks= request.POST.get('marks')
        jeerank= request.POST.get('jeerank')
        upseerank= request.POST.get('upseerank')
        signatureself= request.POST.get('signatureself')
        signatureparent= request.POST.get('signatureparent')
        photo= request.POST.get('photo')
        en=Detail(date=date,branch=branch,rollno=rollno,studentname=studentname,category=category,
                  fathername=fathername,occuption=occuption,income=income,address=address,localguardianname=localguardianname,
                  localguardianaddress=localguardianaddress,mobilenumberguardian=mobilenumberguardian,
                  mobilenumberself=mobilenumberself,mobilenumberfather=mobilenumberfather,
                  mobilenumbermother=mobilenumbermother,emailself=emailself,emailparent=emailparent,
                  accountnumber=accountnumber,ifsc=ifsc,bank=bank,accountholdername=accountholdername,
                  marks=marks,jeerank=jeerank,upseerank=upseerank,signatureself=signatureself,signatureparent=signatureparent,
                  photo=photo)
        en.save()
        return render(request,"form2.html",{'rollno':rollno})

def form3(request):
    if request.method=='POST':
        rollno= request.POST.get('rollno')
        roomnumber= request.POST.get('roomnumber')
        injuries= request.POST.get('injuries')
        allergy= request.POST.get('allergy')
        history= request.POST.get('history')
        declaration= request.POST.get('declaration')
        update = Detail.objects.get(rollno=rollno)
        update.roomnumber = roomnumber
        update.injuries = injuries
        update.allergy = allergy
        update.history = history
        update.declaration = declaration
        update.save()
        return render(request,"form3.html")

def submit(request):
    if request.method=='POST':
        rollno= request.POST.get('rollno')
        draft= request.POST.get('draft')
        draftbankname= request.POST.get('draftbankname')
        favour= request.POST.get('favour')
        update = Detail.objects.get(rollno=rollno)
        update.draft = draft
        update.draftbankname = draftbankname
        update.favour = favour
        update.save()
        return render(request,"home2.html")
    
def data(request,param):
    data = Detail.objects.filter(rollno=param)
    for x in data:
        print(x)
    return render(request,"data2.html",{'data':data})
 


