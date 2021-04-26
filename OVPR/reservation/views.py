from django.shortcuts import render
from django.http import HttpResponse
from pyodbc import IntegrityError
from django.contrib import auth
from django.http import *
from datetime import datetime
from reservation.models import *
from django.utils.datastructures import MultiValueDictKeyError
import random
import pyqrcode

def homepage(request):                          #homepage method
    return render(request,'homepage.html')
def butt(request):                #login method
    return render(request,'next.html',{'value':'Button clicked'})
def but(request):                #contactus page
    return render(request,'Contact.html',{'value':'Button clicked'})

def sign(request):              #signupformpage
    return render(request,'signup form.html',{'value':'Button clicked'})
def bcof(request):                              #booking confirmation page
    return render(request,'Booking Confirmation.html',{'value':'Button clicked'})
def searchresult(request):                          #homepagesearch
    query = request.GET.get('q', '')
    if query:
        qset = (models.Q(Name__icontains=query))
        results = ParkingPlaces.objects.filter(qset).distinct()
    else:
        results = []
    return render(request, "searchresult.html", {"results": results, "query": query})

def selected(request):                          #selecting the searchresult
    p=request.GET['result']
    park=ParkingPlaces.objects.filter(Name=p).values_list()[0]
    return render(request,'searchresult.html',{'var':True,'name':park[0],'Area':park[1],'Total_block':park[2],'available':park[3],'priceperhr':park[4]})

def signedUp(request):
    if request.method != 'POST':
        return render(request,'errorpage.html',{'var':'Wrong Method'})
    else:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phoneno=request.POST['phoneno']
        p1=User(name=name,email=email,phone=phoneno,password=password)
        try:
            p1.save()
        except IntegrityError as ie:
            return render(request,'signedUp.html',{'variable': ie})
        except ValueError as ve:
            return render(request, 'signedUp.html', {'variable': ve})
        return render(request, 'signedUp.html', {'variable': 'signed Up sucess Full please login again'})

# Create your views here.
def vechileregistration(request):
    s=request.GET.get('name')
    return render(request,'vechile_registration1.html',{'name':s})
class Prof:
    global usrobj
    global Name
    global Email
    global Vechile_No
    global BookingFrom
    global BookingTo
    global MobileNo
    global hrs
    global Parking
    global NoOfSlots
    global totPrice
    global basePrice
    global AvailableBlocks
    global msg
    global perslotprice
    global Address
    global Res
    global usrname
    global Tfrom
    global Tto
    global random_id
    global p

    def log(request):
        if request.method != 'POST':
            return render(request, 'errorpage.html', {'var': 'Method wrong'})
        else:
            Prof.usrname = request.POST['username']
            psrd = request.POST['password']
            try:
                Prof.usrobj = User.objects.get(email=Prof.usrname)
            except:
                return render(request, 'next.html', {'var': True})
            else:
                pssd = Prof.usrobj.password
                if psrd == pssd:
                    return render(request, 'Profile.html', {'name': Prof.usrobj.name})
                else:
                    return render(request, 'next.html', {'var': True})
    def prof(request):
        return render(request, 'Profile.html', {'name': Prof.usrobj.name})

    def vechileregistration(request):
        ParkingName=ParkingPlaces.objects.values_list('Name',flat=True)
        return render(request, 'vechile_registration1.html', {'name': Prof.usrobj.name,'items':ParkingName})
    def confirm(request):
        if request.method !='POST':
            return render(request, 'errorpage.html', {'var': 'Method wrong'})
        else:
            Prof.Name=request.POST['name']
            Prof.Email=request.POST['email']
            Prof.Vechile_No=request.POST['vechileNo']
            Prof.BookingFrom=request.POST['BookingFrom']
            Prof.Tfrom=datetime.strptime(Prof.BookingFrom,'%Y-%m-%dT%H:%M')
            Prof.BookingTo=request.POST['BookingTo']
            Prof.Tto=datetime.strptime(Prof.BookingTo,'%Y-%m-%dT%H:%M')
            Prof.MobileNo=request.POST['MobileNo']
            Prof.Parking=request.POST.get('item',None)
            #Prof.NoOfSlots=int(request.POST['Noofslot'])
            TotalBlocks=ParkingPlaces.objects.filter(Name=Prof.Parking).values_list('TotalBlocks',flat=True)[0]
            Prof.AvailableBlocks=ParkingPlaces.objects.filter(Name=Prof.Parking).values_list('AvailableBlocks',flat=True)[0]

            if(Prof.Tto>Prof.Tfrom):
                if(Prof.Tto-Prof.Tfrom).total_seconds()/3600.00>int((Prof.Tto-Prof.Tfrom).total_seconds()/3600) and (Prof.Tto-Prof.Tfrom).total_seconds()/3600.00<int((Prof.Tto-Prof.Tfrom).total_seconds()/3600)+1:
                    Prof.hrs=int(((Prof.Tto-Prof.Tfrom).total_seconds()/3600.00)+1)
                else:
                    Prof.hrs=int((Prof.Tto - Prof.Tfrom).total_seconds() / 3600.00)
            else:
                Prof.msg="BookingTo cannot be less than BookingFrom"
                return render(request, 'vechile_registration1.html', {'name': Prof.usrobj.name,'message':Prof.msg,'var':True})
            if Prof.AvailableBlocks>0:
                Prof.perslotprice=ParkingPlaces.objects.filter(Name=Prof.Parking).values_list('PricePerHr',flat=True)[0]
                Prof.basePrice=Prof.perslotprice*1*Prof.hrs

                Prof.totPrice=Prof.basePrice+(2*(Prof.basePrice*(9/100.00)))
                Prof.random_id = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
            else:
                if Prof.AvailableBlocks<=0:
                    Prof.msg="No slots available."
                    return render(request, 'vechile_registration1.html', {'name': Prof.usrobj.name, 'message': Prof.msg,'var':True})
            return render(request,'Confirmation.html',{'Name':Prof.Name,'Email':Prof.Email,'Place':Prof.Parking,'Vechile_No':Prof.Vechile_No,'hrs':Prof.hrs,'Total_Charge':Prof.basePrice,'grand_total':Prof.totPrice,'No_Of_Slots':'1'})
    def payment(request):
        return render(request, 'Payment.html')
    def sucesspayment(request):
        if request.method!='POST':
            return render(request, 'errorpage.html', {'var': 'Method wrong'})
        else:
            up=ParkingPlaces.objects.get(Name=Prof.Parking)
            up.AvailableBlocks=Prof.AvailableBlocks-1
            up.save()
            s = str(Prof.random_id)
            url = pyqrcode.create(s)   #qrcode
            url.png('templates/media/myqr.png', scale=6)
            Prof.Address=ParkingPlaces.objects.filter(Name=Prof.Parking).values_list('Area',flat=True)[0]
            Prof.Res=Reservation(email=Prof.usrname,Bid=int(Prof.random_id),Name=Prof.Name,parkplace=Prof.Parking,area=Prof.Address,created_time=datetime.now(),start_time=Prof.BookingFrom,end_time=Prof.BookingTo,No_of_hrs=Prof.hrs,Total_price=Prof.totPrice,VhNo=Prof.Vechile_No).save()
            P=Reservation.objects.filter(Bid=int(Prof.random_id)).values_list()
            return render(request, 'Bill.html',{'Bid': P[0][1], 'datetime': P[0][5], 'datetime2': Prof.Tfrom, 'datetime3':Prof.Tto,'Name':Prof.Name,'parkingplace':Prof.Parking,'Loc':Prof.Address,'Vhno':Prof.Vechile_No,'hrs': Prof.hrs,'basePrice':Prof.perslotprice,'NoOfSlot':'1','Price':Prof.basePrice,'total':Prof.totPrice,'name': Prof.usrobj.name})
    def canc(request):
        return render(request,'CancelInput.html',{'name': Prof.usrobj.name})
    def result(request):
        if request.method!='POST':
            return render(request, 'errorpage.html', {'var': 'Method wrong'})
        else:
            bid=int(request.POST['name'])
            Prof.p=Reservation.objects.filter(Bid=bid,email=Prof.usrname)
            if Prof.p:
                return render(request,'CancelInput.html',{'usr':Prof.p[0].email,'Bid':Prof.p[0].Bid,'name':Prof.p[0].Name,'VNo':Prof.p[0].VhNo,'pplace':Prof.p[0].parkplace,'area':Prof.p[0].area,'t1':Prof.p[0].created_time,'t2':Prof.p[0].start_time,'t3':Prof.p[0].end_time,'hrs':Prof.p[0].No_of_hrs,'tot':Prof.p[0].Total_price,'var2':True,'name':Prof.usrobj.name})
            else:
                return render(request,'CancelInput.html',{'var1':True,'name':Prof.usrobj.name})
    def cancel(request):
        cd=ParkingPlaces.objects.get(Name=Prof.p[0].parkplace)
        if cd:
            cd.AvailableBlocks = cd.AvailableBlocks + 1
            cd.save()
            delete=Prof.p.delete()
            if delete:
                return render(request,'sucess.html',{'var':'Sucessfully deleted','name':Prof.usrobj.name})
            else:
                return render(request,'sucess.html',{'var':'UnSucessfully deleted','name':Prof.usrobj.name})
        else:
            return render(request, 'CancelInput.html', {'var1': True})
    def showBooking(request):
        show=Reservation.objects.filter(email=Prof.usrname)
        if show:
            return render(request,'ShowBooking.html',{'var':show,'name': Prof.usrobj.name})
        else:
            return render(request, 'Profile.html', {'var1': True,'name':Prof.usrobj.name})



