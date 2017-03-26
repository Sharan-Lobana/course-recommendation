#!python
#rateapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import *
from .models import *
import main as m
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render

import os
# Create your views here.
# Added a new login view
# Not allowed to view without authenticating

@csrf_protect
def loginview(request):
	loginerror = False
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = None
		# Handle if the username is an emailid
		if '@' in username:
			try:
				user = User.objects.get(email=username)
				username = user.username
			except Exception as e:
				print e
				return render(request,'login.html',{'form':LoginForm(), 'loginerror':True})
		print "NEW METHOD ",username,password
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			#redirect
			return HttpResponseRedirect('/')
		else:
			loginerror = True
	context = {'form': LoginForm(), 'loginerror': loginerror}
	# context['errors'] = loginerror
	return render( request, 'login.html', context)

@csrf_protect
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		# print "FORM    ",form
		print "POST    ",request.POST
		print form.is_valid()
		if form.is_valid():
			try:
				user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
			except Exception as e:
				print "An exception occurred while creating a new user"
				print e
			user.set_password(form.cleaned_data['password1'])
			name_t = form.cleaned_data['name']
			enrollment_t = form.cleaned_data['enrollment']
			semester_t =form.cleaned_data['semester']
			branch_t = form.cleaned_data['branch']
			username_t =form.cleaned_data['username']
			email_t =form.cleaned_data['email']
			print "Adding new entry to UserTable"
			entry = UserTable(
				username = username_t,
				email = email_t,
				name = name_t,
				enrollment = enrollment_t,
				semester = semester_t,
				branch = branch_t,
				hasrated = False
				)
			entry.save()
			print "New Entry Added!"
			return HttpResponseRedirect('/login/')
		else:
			print "Form is not valid"
	else:
		form = RegistrationForm()
	print "Inside REGISTER"
	print request
	print request.body
	print request.method
	context = {'form':form}
	return render( request, 'register.html', context)


@login_required(login_url="login/")
def home(request):
	if request.user.is_authenticated():
		user_django = User.objects.get(id=request.user.id)
		user = UserTable.objects.get(username=user_django.username)
		context = {
		'username':user.username,
		'name':user.name,
		'enrollment_no':user.enrollment,
		'branch':user.branch,
		'semester':user.semester,
		'email':user.email,
		}
		return render(request,"home.html",context)
	else:
		context = {'form': LoginForm(), 'loginerror': False}
		return render(request,"login.html",context)


@login_required(login_url="login/")
@csrf_protect
def rate(request):
	if request.method == 'POST':
		user = User.objects.get(id=request.user.id)
		usert = UserTable.objects.get(username=user.username)
		print request.POST

		# user_val will contain user's prior ratings and current ratings
		user_val = []
		# 29 since there are 29 subjects
		# Initialize user_val with 0
		for i in range(29):
			user_val.append(0)

		# Get the value of previous ratings from the database
		ratings = CourseRating.objects.filter(user_id=usert)
		print "Reached here"
		for i in ratings:
			print "Ratings are: ",
			print i
			course = Course.objects.get(id=i.course_id.id)
			# Course id has the syntax ee-12
			user_val[int(course.course_id[3:])] = i.rating

		prefix = 'sub0'
		# TODO: Modify this range
		for i in range(23,29):
			curKey = prefix+str(i)
			user_val[i] = int(request.POST.get(curKey,'0'))

		print "The value of user_val is: ",
		print user_val
		output, outputarg, courseslist = m.computeRecommendation()
		reco_list = []
		for i in xrange(numcourses):
			temp = []
			j = outputarg[i];

		# Do someting with user_val for computation
		# user_val now contains the rated value of user params
		usert.save()
	else:
		print "Request is not post"
	context = {}
	# context['errors'] = loginerror
	return render( request, 'rate.html', context)

@login_required(login_url="login/")
@csrf_protect
def mycourses(request):
	try:
		user = User.objects.get(id=request.user.id)
		user_t = UserTable.objects.get(username=user.username)

		list_of_courses = []
		for r in CourseRating.objects.filter(user_id=user_t.id):
			c = Course.objects.get(id=r.course_id.id)
			temp = [c.course_name,r.rating,c.semester]
			list_of_courses.append(temp)
		# Keep courses of most recent semester at the top
		list_of_courses.sort(key=lambda x: -x[2])
		return render(request,'mycourses.html',{'mycourseslist':list_of_courses})
	except Exception as e:
		print e
		# TODO: return appropriate response
