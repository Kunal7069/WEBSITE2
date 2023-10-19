from django.contrib import admin
from login.models import Faculty,Student,Detail

class FacultyAdmin(admin.ModelAdmin):
    list_display=('name','username','password')
admin.site.register(Faculty,FacultyAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display=('name','rollno','emailid','username','password')
admin.site.register(Student,StudentAdmin)

class DetailAdmin(admin.ModelAdmin):
    list_display=('date','branch','rollno','studentname','category','fathername','occuption','income','address'
                  ,'localguardianname','localguardianaddress','mobilenumberguardian','mobilenumberself'
                  ,'mobilenumberfather','mobilenumbermother','emailself','emailparent','accountnumber',
                  'ifsc','bank','accountholdername','marks','jeerank','upseerank','signatureself','signatureparent',
                  'photo','roomnumber','injuries','allergy','history','declaration','draft','draftbankname','favour')
admin.site.register(Detail,DetailAdmin)
# Register your models here.

    
    
    