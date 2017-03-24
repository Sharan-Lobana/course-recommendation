from django.contrib.auth.forms import AuthenticationForm 
from django import forms


import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class RegistrationForm(forms.Form):
    semester_choices = (
        ('1','1st'),('2','2nd'),('3','3rd'),('4','4th'),('5','5th'),('6','6th'),('7','7th'),('8','8th'),('9','9th'),('10','10th'),
    )
    branch_choices = (
        ('1','Architecture and Planning'),('2','Applied Science and Engineering'),('3','Biotechnology'),('4','Chemical Engineering'),('5','Chemistry'),('6','Civil Engineering'),('7','Computer Science and Engineering'),('8','Earthquake Engineering'),('9','Earth Sciences'),('10','Electrical Engineering'),
        ('11','Electronics and Communication Engineering'),('12','Humanities and Social Sciences'),('13','Hydrology'),('14','Management Studies'),('15','Mathematics'),('16','Mechanical and Industrial Engineering'),('17','Metallurgical and Materials Engineering'),('18','Paper Technology'),('19','Polymer and Process Engineering'),
        ('20','Physics'),('21','Water Resources Development and Management'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 60, 'required': True, 'class': 'form-control', 'name': 'name'}),label=_("Name"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    enrollment = forms.IntegerField(widget=forms.NumberInput(attrs={'max_length': 30, 'required': True, 'class': 'form-control', 'name': 'enrollment'}), label=_("Enrollment No."))
    semester = forms.ChoiceField(choices = semester_choices, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    branch = forms.ChoiceField(choices = branch_choices, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'max_length': 30, 'required': True, 'class': 'form-control', 'name': 'username'}), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs={'type':'email', 'max_length': 30, 'required': True, 'class': 'form-control', 'name': 'email'}), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'max_length': 30,'min_length' :8, 'render_value': False, 'required': True, 'class': 'form-control', 'name': 'password'}), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'max_length': 30,'min_length' :8, 'render_value': False, 'required': True, 'class': 'form-control', 'name': 'password'}), label=_("Password (again)"))

    
    #def clean_name(self):
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean_password(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data