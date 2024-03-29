from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password= models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=100)
    emailid= models.CharField(max_length=100)
    username = models.CharField(max_length=100, default="username")
    password= models.CharField(max_length=100)

class Detail(models.Model):
    studentname = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    rollno= models.CharField(max_length=100)
    date = models.DateField(max_length=100)
    category= models.CharField(max_length=100)
    fathername= models.CharField(max_length=100)
    occuption= models.CharField(max_length=100)
    income= models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    localguardianname = models.CharField(max_length=100)
    localguardianaddress= models.CharField(max_length=100)
    mobilenumberguardian= models.CharField(max_length=100)
    mobilenumberself= models.CharField(max_length=100)
    mobilenumberfather= models.CharField(max_length=100)
    mobilenumbermother= models.CharField(max_length=100)
    emailself= models.CharField(max_length=100)
    emailparent= models.CharField(max_length=100)
    accountnumber= models.CharField(max_length=100)
    ifsc= models.CharField(max_length=100)
    bank= models.CharField(max_length=100)
    accountholdername= models.CharField(max_length=100)
    marks= models.CharField(max_length=100)
    jeerank= models.CharField(max_length=100)
    upseerank= models.CharField(max_length=100)
    signatureself= models.FileField(upload_to="signatureself/",max_length=250,default=None)
    signatureparent= models.FileField(upload_to="signatureparent/",max_length=250,default=None)
    photo= models.FileField(upload_to="photo/",max_length=250,default=None)
    roomnumber = models.CharField(max_length=100)
    injuries = models.CharField(max_length=500)
    allergy= models.CharField(max_length=500)
    history= models.CharField(max_length=500)
    declaration = models.CharField(max_length=500)
    draft = models.CharField(max_length=100)
    draftbankname = models.CharField(max_length=100)
    favour= models.CharField(max_length=100)
# Create your models here.
