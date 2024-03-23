from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User,AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin","Admin"),
        ("user", "User"),
        ("police","police")
    ]
    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default="user")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    location = models.CharField(max_length=200, null=True)
    profile_image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    guardian_name = models.CharField(max_length=200, null=True)
    guardian_phone = models.CharField(max_length=20, null=True)
    guardian_email = models.EmailField(max_length=30,null=True)

    def __str__(self):
        return self.user.username

class PoliceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="police_profile")
    station_name = models.CharField(max_length=200)
    police_station_location=models.CharField(max_length=200)
    helpline_number = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username

class Complaint(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    status_option={
        ("pending","pending"),
        ("approved","approved")

    }
    status=models.CharField(max_length=200,choices=status_option,default="pending")

    def __str__(self):
        return f"Complaint #{self.pk}"


class Saftytips(models.Model):
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.description
    

class policeofficer(models.Model):

    name=models.CharField(max_length=300)
    phone = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    location = models.CharField(max_length=200, null=True)
    profile_image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    rank=models.CharField(max_length=300)
    station=models.ForeignKey(PoliceProfile,on_delete=models.CASCADE,related_name="police_station")

    def __str__(self):
        return self.name
    


class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.message    



