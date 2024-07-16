from django.db import models
from .choices import GENDER_CHOICES

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=250)
    gender = models.CharField(choices= GENDER_CHOICES, max_length=1)
    dateBth = models.DateTimeField()
    enrolled = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} id:{self.id}"


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    phoneNumber = models.IntegerField()
    emailAddress = models.CharField(max_length=500)
    salary = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} id:{self.id}"
    
class Asignature(models.Model):
     nameAsignature = models.CharField(max_length=200)
     timeperClass = models.IntegerField(max_length=20)
      
     def __str__(self):
        return f"{self.nameAsignature} id:{self.id}"


class Notes(models.Model):
    nameStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    nameTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    nameAsignature = models.ForeignKey(Asignature, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)


    def __str__(self):
        return f"{self.nameStudent} id:{self.id}"

