from django.db import models

photo = models.ImageField(upload_to="gallery")

class ParkingPlaces(models.Model):
    Name=models.CharField(max_length=20,primary_key=True)
    Area=models.CharField(max_length=40)
    TotalBlocks=models.IntegerField()
    AvailableBlocks=models.IntegerField()
    PricePerHr=models.IntegerField()

    def __str__(self):
        return '%s ' '%s ' '%s ' '%s ' '%s ' %(self.Name,self.Area,self.TotalBlocks,self.AvailableBlocks,self.PricePerHr)

class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20,primary_key=True)
    phone=models.IntegerField(max_length=10)
    password=models.CharField(max_length=20)

    def __str__(self):
        return '%s' '%s' '%s' '%s' %(self.name,self.email,self.phone,self.password)
# Create your models here.
class Reservation(models.Model):
    email=models.EmailField()
    Bid=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=100)
    parkplace=models.CharField(max_length=40)
    area=models.CharField(max_length=40)
    created_time=models.DateTimeField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    No_of_hrs=models.IntegerField()
    Total_price=models.DecimalField(max_digits=10,decimal_places=2)
    VhNo=models.CharField(max_length=20)

    def __str__(self):
        return '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' '%s' %(self.email,self.Bid,self.Name,self.parkplace,self.area,self.created_time,self.start_time,self.end_time,self.No_of_hrs,self.Total_price,self.VhNo)