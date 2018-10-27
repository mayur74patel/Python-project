from django.shortcuts import render_to_response,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from login.models import *
#from django.db.models import Q
from django.contrib.auth import *
from login.forms import *

def login1(request):
	c ={}
	c.update(csrf(request))
	c['m']=City.objects.all()
	print(City.objects.all())
	return render_to_response('index.html',c)

def view123(request):
	c ={}
	c.update(csrf(request))
	t=request.POST.get('city','')
	request.session['city']=t
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	try:
		user= Puser.objects.get(user_name=username,password=password)
		request.session['uname']=username
		request.session['psw']=password
		request.session['email']=user.email
		request.session['user_id']=user.user_id
		print("mayur g patel")
		print(user.user_id)
		id=Puser_offer.objects.all().count()
		prof= Puser_offer(user_no=id+1,ur_name=username,psw=password)
		prof.save()
		return HttpResponseRedirect('/login/loggedin/')
	except Exception:
		print("mayur")
		return HttpResponseRedirect('/login/')
	#if user is not None:
	#	return render_to_response('home.html')
	#else:
		

#@login_required(login_url = '/login/')

def loggedin(request):
		try:
			p=request.session['uname']
			return render_to_response('home.html')
		except Exception:
			return HttpResponseRedirect('/login/')
	

def invalidlogin(request):
	return render_to_response('index.html')
	
def signUp(request):
	c ={}
	c.update(csrf(request))
	return render_to_response('signup1.html',c)
def restore(request):
        c={}
        c.update(csrf(request))
        return render_to_response('restore.html',c)
def recover(request):
        return HttpResponse('recover')
        

def store(request):
	id=Puser.objects.all().count()
	username= request.POST.get('username', '')
	request.session['uname'] = username
	password1= request.POST.get('password1', '')
	password2= request.POST.get('password2', '')
	email= request.POST.get('email','')
	phone= request.POST.get('phone', '')
	date= request.POST.get('date', '')
	profile= Puser(user_id=id+1,user_name=username,email=email,phoneno=phone,bdate=date,password=password1)
	profile.save()
	return HttpResponseRedirect('/login/')
	
#

def logout(request):
	del request.session['psw']
	del request.session['email']
	del request.session['user_id']
	del request.session['uname']
	#del request.session['city_id']
	#del request.session["cinema_id"]
	#del request.session['show_id']
	#del request.session['movie_id']
	#del request.session['movie']
	#del request.session['time']
	#del request.session['theatre']
	del request.session['city']
	#del request.session['video']
	
	return HttpResponseRedirect('/login/')
def cinema(request):
	try:	
		patel=request.session["uname"]
		c=request.session['city']
		print(c)
		p=City.objects.get(city_name=c)
		t=p.city_id
		request.session['city_id']=t
		print(t)
		q=C_city.objects.filter(city_id=t)
		student={
			"cinema_number": q
				}
		return render_to_response('cinema.html',student)
	except Exception:
			return HttpResponseRedirect('/login/')	
def Profile(request):
		c ={}
		c.update(csrf(request))
		n1=request.GET.get('id1', '')
		n2=request.GET.get('id2','')
		l=request.session["uname"]
		l1=request.session['psw']
		p=Puser_offer.objects.filter(ur_name=l,psw=l1)
		print(len(list(p)))
		p1=len(list(p))
		if (p1>10):
			c['t4']="you are available to offer"
		if n1:
			Ticket_N.objects.filter(user_name=l,movie_name=n1,city_name=n2).delete()
			c['t3']=Ticket_N.objects.filter(user_name=l)
		else:
			c['t3']=Ticket_N.objects.filter(user_name=l)
		
		c['t1']=request.session['uname'].capitalize()
		c['t2']=request.session['email']
		
		return render_to_response('profile.html',c)
def movie(request):
	c ={}
	c.update(csrf(request))
	try:
		patel=request.session["uname"]
		number=request.GET.get('id', '')
		name=request.GET.get('id1','')
		request.session['theatre']=name
		print(name)
		request.session["cinema_id"]=number
		
		data = Movie.objects.all()
		c['h1']=data
		c['h2']=number
	
	
#i=0
#for student in data
#	if student.cinema_id_id == number
#		m[i]=student.movie_id
#		request.session("movie_name
#		i=i+1
	
	#student={
	#	"movie_number": data
	#		}
		return render(request,'movies.html',c)
	except Exception:
		return HttpResponseRedirect('/login/')
def book(request):
	c={}
	c.update(csrf(request))
	try:
		tm=request.GET.get('id', '')
		tm1=request.GET.get('id1', '')
		request.session['time']=tm
		request.session['show_id']=tm1
		patel=request.session["uname"]
		c['t1']=patel
		c['t2']=request.session['video']
		return render_to_response('book.html',c)
	except Exception:
		return HttpResponseRedirect('/login/')
def show(request):
	c={}
	
	number1=request.GET.get('id1', '')
	name=request.GET.get('id2','')
	request.session['movie_id']=number1
	request.session['movie']=name
	show_data=Show.objects.filter(movie_id_id=number1)
	show_movie=Movie.objects.all()
	p=Movie.objects.get(movie_id=number1)
	request.session["video"]=p.movie_vid
	c['t1']=show_data
	c['t2']=number1
#	c['t3']=show_movie
	print(show_movie)
	print(number1)
	return render_to_response('show.html',c)

def pay(request):
	c={}
	c.update(csrf(request))
	used=[]
	p=[]
	rate=0
	c12=request.POST.getlist('seat','')
	l1=len(c12)
	print(c12)
	unique = [used.append(x) for x in c12 if x not in used]
	#print(used)
	
	u_id=request.session['user_id']
	ct_id=request.session['city_id']
	c_id=request.session["cinema_id"]
	s_id=request.session['show_id']
	m_id=request.session['movie_id']
	m_name=request.session['movie']
	s_name=request.session['time']
	u_name=request.session["uname"]
	c_name=request.session['theatre']
	ct_name=request.session['city']
	print("counter")
#	profile=Ticket_D(ticket_name=used,movie_id=m_id,cinema_id=c_id,city_id=ct_id,show_id=s_id,user_id=user.user_id)
	profile=Ticket_N(ticket_name=used,user_name_id=u_id,user_name=u_name,cinema_name=c_name,movie_name=m_name,city_name=ct_name,show_name=s_name)
	profile.save()
	request.session['ticket']=used
	
	l=len(used)
	print("mayur")
	print(c)
	print("mayur")
	for i in range (0,l):
		p.append(list(used[i]))
		t=p[i]
		m=len(t)
		for i in range(0,m):
			if t[i] == 'A':
				rate=rate+100
			if t[i] == 'B':
				rate=rate+150
			if t[i] == 'C':
				rate=rate+200
			if t[i] == 'D':
				rate=rate+250
			if t[i] == 'E':
				rate=rate+300
			if t[i] == 'F':
				rate=rate+300
			if t[i] == 'G':
				rate=rate+300
			if t[i] == 'H':
				rate=rate+300
			if t[i] == 'I':
				rate=rate+300
			if t[i] == 'J':
				rate=rate+300
			if t[i] == 'K':
				rate=rate+300
	print(rate)
	rate1=rate*0.18
	rate2=1.18*rate
	c['t1']=rate
	c['t2']=rate1
	c['t3']=rate2
	request.session['total']=rate2
	c['t4']=used
	c['t5']=request.session["uname"]
	return render_to_response('Bill.html',c)
#	except Exception:
#			return HttpResponseRedirect('/login/')
def payment(request):
	c={}
	c.update(csrf(request))
	try:
		c['t5']=request.session["uname"]
		return render_to_response('Payment.html',c)
	except Exception:
			return HttpResponseRedirect('/login/')
def success(request):
	c={}
	c.update(csrf(request))
	ac=request.POST.get('Account Name','')
	c['t1']=request.session['uname'].capitalize()
	c['t2']=request.session['city']
	c['t3']=request.session['total']
	c['t4']=request.session['ticket']
	c['t5']=request.session['email']
	c['t6']=request.session['theatre']
	c['t7']=request.session['movie']
	c['t8']=request.session['time']
	return render_to_response('Success.html',c)
	
def admin(request):
	c={}
	c.update(csrf(request))
	return render_to_response('admin_login.html',c)
	
def admin_check(request):
	c={}
	c.update(csrf(request))
	c['msg']="please enter valid data"
	a_name=request.POST.get('adminname','')
	a_psw=request.POST.get('adminpassword','')
	try:
		user=admin_detail.objects.get(admin_name=a_name,admin_password=a_psw)
		request.session['admin_name']=a_name
		request.session['admin_psw']=a_psw
		return render_to_response('admin_add_movie.html',c)
	except Exception:	
		return HttpResponseRedirect('/login/admin1/',c)
def admin_signup(request):
	c={}
	c.update(csrf(request))
	return render_to_response('admin_signup.html',c)

def admin_store(request):
	c={}
	c.update(csrf(request))
	
	a_name=request.POST.get('adminname','')
	print(a_name)
	a_psw=request.POST.get('password','')
	a_mo=request.POST.get('admin_phone','')
	a_email=request.POST.get('admin_email','')
	a_city=request.POST.get('admin_city','')
	a_cinema=request.POST.get('admin_cinema','')
	profile=admin_detail(admin_name=a_name,admin_password=a_psw,admin_cinema_work=a_cinema,admin_city_work=a_city,admin_email_id=a_email,admin_mobile_no=a_mo)
	profile.save()
	a_name=request.session['admin_name']
	a_psw=request.session['admin_psw']
		
	user=admin_detail.objects.get(admin_name=a_name,admin_password=a_psw)
		
	t1=user.admin_cinema_work
	request.session['cinema_work']=t1
	t2=user.admin_city_work
	print(t1)
	print(t2)
	pf1=City.objects.all().count()
	try:#this is not a exception error
		pf=City.objects.get(city_name=t2)
		print("check object")
		print(pf)	
	except Exception:
		p=City(city_id=pf1+1,city_name=t2)
		p.save()
		pf=City.objects.get(city_name=t2)
		
		a_city_id=pf1+1
		print(p)
		pf2=Cinema1.objects.all().count()
		try:
			pff=Cinema1.objects.get(cinema_name=t1)
			#request.session['Cinema_obj']=pff
			a_cinema_id=pff.cinema_id
			#	print(pff)	
			print("mayur")
		except Exception:
			p=Cinema1(cinema_id=pf2+1,cinema_name=t1)
			pff=Cinema1.objects.get(cinema_name=t1)
			#request.session['Cinema_obj']=pff
			request.session['t123']=t1
			p.save()
			a_cinema_id=pf2+1
			print(p)
		try:
			pf3=C_city.objects.get(cinema_id=pff,city_id=pf)
			print("mayur patel")
		except Exception:
			print("ys")
			print(pff.cinema_id)
			p=C_city(cinema_id=pff,city_id=pf)
			p.save()
			print("ys")
		
	return HttpResponseRedirect('/login/admin1/')
def add_movie(request):
	c={}
	c.update(csrf(request))
	m=request.POST.get('Movie','')
	m_detail=request.POST.get('Movie_detail','')
	d=request.POST.get('date','')
	m_i=request.POST.get('Movie_image','')
	m_v=request.POST.get('Movie_video','')
	
	print(m_i)
	#tat=request.session['t123']
	#cinema_name=request.session['cinema_work']
	try:
		obj=request.session['Cinema_obj']
	except Exception:
	
		t=request.POST.get('time','')
		p2=Movie.objects.all().count()
		p3=Show.objects.all().count()
	try:
		dat = Movie.objects.get(movie_name=m,cinema_id=obj)
		try:
			da=Show.objects.get(movie_id=dat,time=t,cinema_id=obj)
			print("error occur in movie-show available")
			return HttpResponseRedirect('/login/admin1/')
		except Exception:
			daa=Show(show_id=p3+1,movie_id=dat,cinema_id=obj,time=t)
			daa.save()
			print("error occur in movie available,show not available")
			return HttpResponseRedirect('/login/admin1/')
	except Exception:
		data=Movie(movie_id=p2+1,movie_name=m,cinema_id=obj,movie_detail=m_detail,movie_img=m_i,movie_vid=m_v)
		data.save()
		dat = Movie.objects.get(movie_name=m,cinema_id=obj)
		try:
			da=Show.objects.get(movie_id=dat,time=t,cinema_id=obj)
			print("error occur in movie not but added available show is available")
			return HttpResponseRedirect('/login/admin1/')
		except Exception:
			daa=Show(show_id=p3+1,movie_id=dat,cinema_id=obj,time=t)
			daa.save()
			print("error occur in movie not but added available show is available")
			return HttpResponseRedirect('/login/admin1/')
	