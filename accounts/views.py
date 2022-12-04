from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .models import Patient,Doctor
from prescriptions.models import Prescription
from django.contrib import messages
import datetime
from django.core.mail import send_mail
import random
from reportlab.pdfgen    import canvas
from reportlab.lib.utils import ImageReader
from datetime            import datetime
from django.http import HttpResponse
from django.http import FileResponse

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        phone=request.POST['phone']
        typ=request.POST['type']
        if pass1==pass2:
            if User.objects.filter(username=email).exists():
                messages.info(request,"Email Id already Exists!")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=fname,last_name=typ,username=email,password=pass1,email=email)
                o=str(random.randint(100000,999999))
                if typ=="Doctor":
                    pro=Doctor(user=user,phone=phone,otp=o)
                    pro.save()
                    m='Hey '+fname+'!\n'+'Thank you for registering with the Hospital Management!\n\n'+'Your OTP is :'+o
                    send_mail('Registration Successful!',m,'Hospital Management',[email],fail_silently=True)
                    messages.info(request,"Account Created Successfully")
                    return redirect('login')
                if typ=="Patient":
                    pro=Patient(user=user,phone=phone,otp=o)
                    pro.save()
                    m='Hey '+fname+'!\n'+'Thank you for registering with the Hospital Management!\n\n'+'Your OTP is :'+o
                    send_mail('Registration Successful!',m,'Hospital Management',[email],fail_silently=True)
                    messages.info(request,"Account Created Successfully")
                    return redirect('login')
        else:
            messages.info(request,"Passwords didn't matched!")
            return redirect('register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.last_name=="Reception":
                return redirect('reception')
            if request.user.last_name=="HR":
                return redirect('dashboard')
            if user.last_name=="Doctor":
                pro=Doctor.objects.filter(user=user).first()
            if user.last_name=="Patient":
                pro=Patient.objects.filter(user=user).first()
            return redirect('uprofile')
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('login')
    else:
        return render(request,'accounts/login.html')



@login_required
def uprofile(request):
    if request.user.last_name=='Doctor':
        pro=Doctor.objects.filter(user=request.user).first()
    if request.user.last_name=='Patient':
        pro=Patient.objects.filter(user=request.user).first()
    if request.user.last_name=='Reception':
        pid=request.POST['pid']
        pro=Patient.objects.filter(pid=pid).first()
    if request.method=='POST':
        if request.user.last_name=='Reception':
            pid=request.POST['pid']
            pro=Patient.objects.filter(pid=pid).first()
        if request.user.last_name=='HR':
            pid=request.POST['pid']
            pro=Doctor.objects.filter(did=pid).first()
        try:
            _, file = request.FILES.popitem()
            file = file[0]
            pro.image = file
        except:
            pass
        finally:
            pro.phone=request.POST['phone']
            pro.age=request.POST['age']
            pro.gender=request.POST['gender']
            if pro.user.last_name=='Patient':
                pro.address=request.POST['address']
                pro.government_id=request.POST['government_id']
                pro.caregiver=request.POST['caregiver']
            if pro.user.last_name=='Doctor':
                pro.status=request.POST['status']
                pro.salary=request.POST['salary']
                pro.Department=request.POST['dept']
                pro.attendance=request.POST['attn']
            pro.save()
            if request.user.last_name=='Reception':
                return redirect("reception")
            if request.user.last_name=='HR':
                return redirect("dashboard")
            return redirect('profile')
    c={'pro':pro}
    return render(request,'accounts/uprofile.html',c)


@login_required
def profile(request):
    if request.user.last_name=='Doctor':
        pro=Doctor.objects.filter(user=request.user).first()
    if request.user.last_name=='Patient':
        pro=Patient.objects.filter(user=request.user).first()
    c={'pro':pro}
    return render(request,'accounts/profile.html',c)



@login_required
def list_patients(request):
    pro=Patient.objects.all()
    c={'pat':pro}
    return render(request,'accounts/list_patients.html',c)

@login_required
def generate_pdf(request, pk):
    pro=Patient.objects.filter(pid=pk).first()
    pres = Prescription.objects.filter(patient = pro).all()

    response = HttpResponse(content_type='application/pdf') 

    # Create the PDF object, using the response object as its "file." 
    p = canvas.Canvas(response)     
    p.drawString(100, 800, str(pro.pid)+' ' +str(pro.phone)+' ' + str(pro.user.first_name))
    i = 0
    for pre in pres:
        p.drawString(100, 770-i, str(pre.prid)+ ' '+str(pre.doctor)+ ' '+ pre.disease+' ' + pre.prescription +''+ str(pre.date))
        i+=30



    # Close the PDF object. 
    p.showPage() 
    p.save() 

    # Show the result to the user    
    redirect('list_patients/'+str(pk))
    
    return response


@login_required
def patient_detail(request, pk):

    pro=Patient.objects.filter(pid=pk).first()
    pres = Prescription.objects.filter(patient = pro)

    c={'pat':pro, 'pres' :pres}
    return render(request,'accounts/patient_detail.html',c)




def logout(request):
    auth.logout(request)
    return redirect('login')

def contactus(request):
     return render(request,'accounts/contactus.html')