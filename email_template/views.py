from django.shortcuts import render

# Create your views here.
from email_template.models import employee
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse
from datetime import date

print('hi===================================================================================')
def birthday(request):
    print("________________________________________________________________________________________________start")
    p=employee.objects.all()
    #print('============================ok')
    l=[]
    for i in p:

        j=date.today()

        if(int(j.month)==int(i.employee_birthday_month) and int(j.day)==int(i.employee_birthday_date)):
            l.append(i.employee_id)
            print(l,'listttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt')
            print('=====================================================================================================')
    print(l)







        #x="arushijhalani9220@gmail.com"
    #y="priyanshjhalani25@gmail.com"
    sender="priyanshjhalani0@gmail.com"
        #sender="priyanshjhalani30@gmail.com"
    for i in l:
        print(i,'==================================================================================')
        k=employee.objects.get(employee_id=i)
        print(k.employee_name,'==============================================================')
        print(k.employee_email,'==============================================================')
        templt=render_to_string('xyz.html',{'Name':'arpit'})

        send_mail(
        'For birthday wish',
            "Happy birthday  {}".format(k.employee_name),


        sender,
        [k.employee_email],
        fail_silently=False,html_message=templt
        )
    return HttpResponse("ok")

def x(request):
    templt=render_to_string('xyz.html',{'Name':'arpit'})

    send_mail(
        'For birthday wish',
            "Happy birthday  {}",


        'priyanshjhalani0@gmail.com',
        ['deykaran07@gmail.com'],
        fail_silently=False,html_message=templt
        )
    return HttpResponse("ok")