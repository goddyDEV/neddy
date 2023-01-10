from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.forms import ValidationError

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    about_image = models.ImageField(upload_to="about/%Y-%m-%d", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Hero(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class HeroImage(models.Model):
    hero = models.ForeignKey(Hero, null=True, blank=True, on_delete=models.CASCADE)
    hero_image = models.ImageField(upload_to="hero/%Y-%m-%d", default='hero/default.jpg')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.hero_image)


class Testmony(models.Model):
    image = models.ImageField(upload_to="testmony/%Y-%m-%d", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image     


class SocialMedia(models.Model):
    CHOICE = [
        ('facebook','facebook'),
        ('twitter','twitter'),
        ('linkedin','linkedin'),
        ('instagram','instagram'),
        ('tiktok','tiktok'),
    ]
    name = models.CharField(choices=CHOICE,max_length=100)
    link = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name               



class Settings(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    url = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to="logo/%Y-%m-%d")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name        


class Service(models.Model):
    CHOICE = [
        ('Graphics','Graphics'),
        ('Photography','Photography'),
        ('Videography','Videography'),
    ]
    category = models.CharField(choices=CHOICE,max_length=100)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    file = models.FileField(upload_to="uploads/%Y-%m-%d")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Team(models.Model):
    CHOICE = [
        ('Managing Director','Managing Director'),
        ('Designer','Designer'),
        ('Photographer','Photographer'),
        ('Videographer','Videographer'),
    ]
    name = models.CharField(max_length=100, unique=True)
    position = models.CharField(choices=CHOICE,max_length=100)
    image = models.ImageField(upload_to="images/%Y-%m-%d")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title       
             


class Order(models.Model):
    CHOICE = [
        ('On Progress','On Progress'),
        ('Received','Received'),
        ('Delivery','Delivery'),
        ('Canceled','Canceled'),
    ]
    fullname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(null=True, blank=True )
    date_start = models.DateField(null=True, blank=True)
    date_delivery = models.DateField()
    status = models.CharField(choices=CHOICE,max_length=100, default="Received")
    received_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


    # @property
    # def is_past_due(self):
    #     return date.today() > self.date_start

