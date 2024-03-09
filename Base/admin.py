from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['parent_id', 'first_name', 'last_name', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['first_name', 'last_name', 'email']

@admin.register(models.Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ['child_id', 'child_name', "child_sex", 'date_of_birth', 'age', 'parent' ]
    search_fields = ['child_name', 'date_of_birth']
    list_filter = ['child_name', 'date_of_birth']

@admin.register(models.PolioDetails)
class PolioDetailsAdmin(admin.ModelAdmin):
    list_display = ['polio_id', 'child', 'dose_1_date', 'dose_2_date', 'dose_3_date', 'booster_dose_date']
    search_fields = ['child__child_name']
    list_filter = ['child__child_name']

@admin.register(models.Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ['vaccine_id', 'vaccine_name', 'manufacturer', 'disease_targeted', 'approval_status', 'dosage', 'storage_requirements', 'efficacy', 'side_effects', "approval_status", "date_of_approval", "distribution_status" ,"country_region_approval", 'cost', 'additional_notes', "image"]
    search_fields = ['vaccine_name', 'manufacturer']
    list_filter = ['vaccine_name', 'manufacturer']

@admin.register(models.VaccineStatus)
class VaccineStatusAdmin(admin.ModelAdmin):
    list_display = ['vaccine', 'child', 'completed']
    search_fields = ['vaccine', 'child']
    list_filter = ['vaccine', 'child']

@admin.register(models.Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['disease_id', 'disease_name', 'description']
    search_fields = ['disease_name', 'description']
    list_filter = ['disease_name', 'description']

@admin.register(models.Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ['nutrition_id', 'nutrition_name', 'age_group', 'feeding_method', 'introduction_of_solids', 'recommended_diet']
    search_fields = ['nutrition_name']
    list_filter = ['nutrition_name']

@admin.register(models.Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_id', 'doctor_name', 'email', 'phone_number', 'specialization', 'hospital']
    search_fields = ['doctor_name', 'email']
    list_filter = ['doctor_name', 'email']

@admin.register(models.Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['hospital_id', 'hospital_name', 'address', 'city', 'country', 'phone_number']
    search_fields = ['hospital_name']
    list_filter = ['hospital_name']

@admin.register(models.Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']