from django.db import models
import django.utils.timezone

class Puser(models.Model):
	user_id=models.CharField(max_length=30,primary_key='true')
	user_name=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	phoneno=models.IntegerField();
	bdate=models.DateTimeField();
	password=models.CharField(max_length=20)

class Puser_offer(models.Model):
	user_no=models.CharField(max_length=30,primary_key='true')
	ur_name=models.CharField(max_length=30)
	psw=models.CharField(max_length=20)	
	
class Offers(models.Model):
	offer_id=models.CharField(max_length=30,primary_key='true')
	offer_details=models.TextField()
	
class Ticket(models.Model):
	ticket_id=models.CharField(max_length=30,primary_key='true')
	user_id=models.ForeignKey('Puser',on_delete='true')
	show_id=models.ForeignKey('Show',on_delete='true')

class Movie(models.Model):
	movie_id=models.CharField(max_length=30,primary_key='true')
	cinema_id=models.ForeignKey('Cinema1',on_delete='true')
	movie_name=models.CharField(max_length=50)
	movie_details=models.TextField()
	movie_pic=models.ImageField()
	movie_img=models.CharField(max_length=100)
	movie_vid=models.CharField(max_length=100)
	
class Cinema1(models.Model):
	cinema_id=models.CharField(max_length=30,primary_key='true')
	cinema_name=models.CharField(max_length=50)
	cinema_details=models.TextField()
	
class Show(models.Model):
	show_id=models.CharField(max_length=30,primary_key='true')
	cinema_id=models.ForeignKey('Cinema1',on_delete='true')
	movie_id=models.ForeignKey('Movie',on_delete='true')
	time=models.DateTimeField()
	
class TicketOffer(models.Model):
	ticket_id=models.ForeignKey('Ticket',on_delete='true')
	offer_id=models.ForeignKey('Offers',on_delete='true')

class Random(models.Model):
	random_id=models.CharField(max_length=30,primary_key='true')
	random_name=models.CharField(max_length=50)

class City(models.Model):
	city_id=models.CharField(max_length=30,primary_key='true')
	city_name=models.CharField(max_length=50)
	
class C_city(models.Model):
	city_id=models.ForeignKey('City',on_delete='true')
	cinema_id=models.ForeignKey('Cinema1',on_delete='true')
	
class Ticket_D(models.Model):
	ticket_name=models.CharField(max_length=30)	
	user_id=models.ForeignKey('Puser',on_delete='true')
	show_id=models.ForeignKey('Show',on_delete='true')
	city_id=models.ForeignKey('City',on_delete='true')
	cinema_id=models.ForeignKey('Cinema1',on_delete='true')
	movie_id=models.ForeignKey('Movie',on_delete='true')

class Ticket_N(models.Model):	
	ticket_name=models.CharField(max_length=30)
	user_name_id=models.CharField(max_length=30)
	user_name=models.CharField(max_length=30)
	cinema_name=models.CharField(max_length=30)
	movie_name=models.CharField(max_length=30)
	show_name=models.CharField(max_length=30)
	city_name=models.CharField(max_length=30)

class admin_detail(models.Model):
	admin_name=models.CharField(max_length=30)
	admin_password=models.CharField(max_length=30)
	admin_cinema_work=models.CharField(max_length=30)
	admin_city_work=models.CharField(max_length=30)
	admin_email_id=models.CharField(max_length=30)
	admin_mobile_no=models.CharField(max_length=30)
	