from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserTable(models.Model):
	# Fields of the database here
	semester_choices = (
	    ('1','1st'),('2','2nd'),('3','3rd'),('4','4th'),('5','5th'),('6','6th'),('7','7th'),('8','8th'),('9','9th'),('10','10th'),
	)
	branch_choices = (
	    ('1','Architecture and Planning'),('2','Applied Science and Engineering'),('3','Biotechnology'),('4','Chemical Engineering'),('5','Chemistry'),('6','Civil Engineering'),('7','Computer Science and Engineering'),('8','Earthquake Engineering'),('9','Earth Sciences'),('10','Electrical Engineering'),
	    ('11','Electronics and Communication Engineering'),('12','Humanities and Social Sciences'),('13','Hydrology'),('14','Management Studies'),('15','Mathematics'),('16','Mechanical and Industrial Engineering'),('17','Metallurgical and Materials Engineering'),('18','Paper Technology'),('19','Polymer and Process Engineering'),
	    ('20','Physics'),('21','Water Resources Development and Management'),
	)
	username = models.CharField(max_length=30,unique=True)
	name = models.CharField(max_length=60)
	email = models.EmailField(max_length=254)
	enrollment = models.IntegerField(unique=True)
	semester = models.CharField(max_length=2, choices = semester_choices, default = '1')
	branch = models.CharField(max_length=5, choices = branch_choices, default = '1')
	hasrated = models.BooleanField(default = False)