from django.db import models


# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=200)
    AdmissionNumber = models.IntegerField()
    Course = models.CharField(max_length=200)

    class Meta:
        db_table = "Student"
