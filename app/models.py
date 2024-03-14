from django.db import models
from django.utils.text import slugify
# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    name = models.CharField(max_length = 200)
    compony = models.CharField(max_length = 200)
    designation = models.CharField(max_length = 200)
    
    def __str__(self):
        return f'Written By {self.name}' 

class Location(models.Model):
    street = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length =200)
    country = models.CharField(max_length = 200)
    zip = models.CharField(max_length = 200)
    
    def __str__(self):
        return f"{self.street} Street, {self.city} "

class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time',"Full Time"),
        ('Part Time',"Part Time"),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    expiry = models.DateField(null = True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True, max_length=40, unique = True)  
    location = models.OneToOneField(Location,on_delete = models.CASCADE ,null = True)  
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null =True)
    skills = models.ManyToManyField(Skills)
    type= models.CharField(max_length=200,null=False , choices= JOB_TYPE_CHOICES)
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(JobPost,self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.title} with salary {self.salary}"
    
    
    
