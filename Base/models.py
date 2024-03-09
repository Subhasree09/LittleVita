from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    user = models.OneToOneField(User, null=True,blank = True, on_delete=models.CASCADE)
    parent_id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    dp= models.ImageField(upload_to='parent_images/', default='default_dp.jpg', null=True, blank=True)
    # Add other parent details as needed

    def __str__(self):
        return self.first_name


class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    child_name = models.CharField(max_length=100, null=True, blank=True)
    child_sex = models.CharField(max_length=10, default='Undefined')
    date_of_birth = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey(Parent, related_name='children', on_delete=models.CASCADE)
    vaccine = models.ManyToManyField('Vaccine', through='VaccineStatus', related_name='children', null=True, blank=True)

    # Add other child details as needed

    def __str__(self):
        return self.child_name

class PolioDetails(models.Model):
    polio_id = models.AutoField(primary_key=True)
    child = models.OneToOneField('Child', related_name='polio_details', on_delete=models.CASCADE)
    dose_1_date = models.DateField(null=True, blank=True)
    dose_2_date = models.DateField(null=True, blank=True)
    dose_3_date = models.DateField(null=True, blank=True)
    booster_dose_date = models.DateField(null=True, blank=True)
    # Add other polio dose details as needed

    def __str__(self):
        return f"Polio Details for {self.child.child_name}"


class Vaccine(models.Model):
    vaccine_id = models.AutoField(primary_key=True)
    vaccine_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    disease_targeted = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50, null=True, blank=True)
    storage_requirements = models.CharField(max_length=100)
    efficacy = models.CharField(max_length=100, null=True, blank=True)
    side_effects = models.TextField(null=True, blank=True)
    approval_status = models.CharField(max_length=50)
    date_of_approval = models.DateField(null=True, blank=True)
    distribution_status = models.CharField(max_length=50)
    country_region_approval = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    additional_notes = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='vaccin_images/', null=True, blank=True)
    child = models.ManyToManyField('Child', through='VaccineStatus', related_name='vaccines')

    
    def __str__(self):
        return self.vaccine_name
    
class VaccineStatus(models.Model):
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    vaccine = models.ForeignKey('Vaccine', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.child.child_name} - {self.vaccine.vaccine_name} ({'Completed' if self.completed else 'Not Completed'})"

class Disease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name = models.CharField(max_length=100)
    description = models.TextField()
    symptoms = models.TextField()
    treatment = models.TextField()
    prevention = models.TextField()
    image = models.ImageField(upload_to='disease_images/', null=True, blank=True)
    
    def __str__(self):
        return self.disease_name
    

class Nutrition(models.Model):
    nutrition_id = models.AutoField(primary_key=True)
    nutrition_name = models.CharField(max_length=100, default="Nutrition Name Unavailable")
    age_group = models.CharField(max_length=50)
    feeding_method = models.CharField(max_length=100)
    
    introduction_of_solids = models.TextField(null=True, blank=True, default="Not applicable")
    recommended_diet = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='nutrition_images/', blank=True, null=True)

    
    def __str__(self):
        return f"Nutrition for {self.age_group}"
    
class Day(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    hospital = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_images/', default='default_image.jpg')
    time = models.CharField(max_length=100, default="10:00-18:00")
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    days_in_hospital = models.ManyToManyField(Day)
    # Add other fields as needed

    def __str__(self):
        return self.doctor_name



    

class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    # Add other fields as needed

    def __str__(self):
        return self.hospital_name