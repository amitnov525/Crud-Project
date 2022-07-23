from django.contrib import admin
from main.models import Student1

# Register your models here.
@admin.register(Student1)
class show(admin.ModelAdmin):
    list_display=['id','name','email','password']
