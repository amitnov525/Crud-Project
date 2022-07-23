from django import forms
from main.models import Student1

class Student(forms.ModelForm):
    class Meta:
        model=Student1
        fields=['name','email','password']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'})}
        
        
