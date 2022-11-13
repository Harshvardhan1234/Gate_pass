from django.shortcuts import render
from django.shortcuts import redirect

from datetime import datetime
from datetime import date

import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd


def mail1():

    datex = date.today()
    timex = datetime.today().strftime("%I:%M %p")
    messx  = str("Dear Harshavardhan S V")+'''<br><br>'''+str("Your outing request has been approved for the below mentioned date and time.<br><br")+'''
    test<br>
    Date: '''+str(datex)+'''<br>
    Time: '''+str(timex)+'''<br><br>
    Regards<br>
    Hostel Administration<br>       
    
    '''
    html = messx
    email_from = 'hostelkctll@gmail.com'
    password = 'gezftuozggpaicls'
    email_to = 'harshavardhan.20cs@kct.ac.in'
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')
    email_message = MIMEMultipart()
    email_message['From'] = 'Hostel KCT'
    email_message['To'] = email_to
    # email_message['Subject'] = f'Report email - {date_str}'
    email_message['Subject'] = "Outing Request Approved- Harshavardhan SV 20BCS040"
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)



def mail2(timey):

    datex = date.today()
    timex = timey
    messx  = str("Dear Harshavardhan S V")+'''<br><br>'''+str("Your outing request has been approved for the below mentioned date and time.<br><br")+'''
    test<br>
    Date: '''+str(datex)+'''<br>
    Time: '''+str(timex)+'''<br><br>
    Regards<br>
    Hostel Administration<br>       
    
    '''
    html = messx
    email_from = 'hostelkctll@gmail.com'
    password = 'gezftuozggpaicls'
    email_to = 'harshavardhan.20cs@kct.ac.in'
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')
    email_message = MIMEMultipart()
    email_message['From'] = 'Hostel KCT'
    email_message['To'] = email_to
    # email_message['Subject'] = f'Report email - {date_str}'
    email_message['Subject'] = "Outing Request Approved- Harshavardhan SV 20BCS040"
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)




def  mail3(name,email,roll_no,timey):

    datex = date.today()
    timex = timey
    messx  = "Dear "+name+" "+'''<br><br>'''+str("Your outing request has been approved for the below mentioned date and time.<br><br")+'''
    test<br>
    Date: '''+str(datex)+'''<br>
    Time: '''+str(timex)+'''<br><br>
    Regards<br>
    Hostel Administration<br>       
    
    '''
    html = messx
    email_from = 'hostelkctll@gmail.com'
    password = 'gezftuozggpaicls'
    email_to = email
    date_str = pd.Timestamp.today().strftime('%Y-%m-%d')
    email_message = MIMEMultipart()
    email_message['From'] = 'Hostel KCT'
    email_message['To'] = email_to
    # email_message['Subject'] = f'Report email - {date_str}'
    email_message['Subject'] = "Outing Request Approved- "+name+" "+roll_no
    email_message.attach(MIMEText(html, "html"))
    # Convert it as a string
    email_string = email_message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_from, password)
        server.sendmail(email_from, email_to, email_string)





def home(request):
    return render(request,'home.html')


def only_my_name(request):
    mail1()
    
    # return render(request,'home.html')
    
    return redirect('/')


def with_time(request):
    
    time = request.POST["timing"]
    mail2(time)   
    # return render(request,'home.html')
    return redirect('/')

def with_details(request):
    name = request.POST["name"]
    email = request.POST["email"]
    roll_no = request.POST["roll_no"]
    time = request.POST["time"]
    print("\n\n\n",name,email,roll_no,time,"\n\n\n")
    
    mail3(name,email,roll_no,time)
    
    # return render(request,'home.html')
    return redirect('/')


