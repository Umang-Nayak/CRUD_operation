from django.db import models

# Create your models here.


class Employee(models.Model):
    e_id = models.AutoField(primary_key=True)
    e_fname = models.CharField(max_length=50)
    e_lname = models.CharField(max_length=50)
    e_contact = models.CharField(max_length=13)
    e_address = models.CharField(max_length=250)
    e_email = models.EmailField(max_length=100)
    e_password = models.CharField(max_length=50)

    class Meta:
        db_table = "employee"
