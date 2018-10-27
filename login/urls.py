from django.urls import path
from . import views

urlpatterns = [
    path('', views.login1),
	path('admin1/',views.admin),
	path('check/',views.admin_check),
	path('adminSignup/',views.admin_signup),
    path('view/', views.view123),
    path('loggedin/', views.loggedin),
    path('invalidlogin/', views.invalidlogin),
    path('signUp/', views.signUp),
    path('store/',views.store),
	path('adminstore/',views.admin_store),
    path('restore/',views.restore),
    path('recover/',views.recover),
	path('cinema/',views.cinema),
	path('profile/',views.Profile),
    path('movies/',views.movie),
	path('cinema/show/',views.show),
	path('cinema/book/',views.book),
	path('cinema/book/pay',views.pay),
    path('cinema/book/pay/payment',views.payment),
	path('cinema/book/pay/payment/success',views.success),
    path('addmovie/',views.add_movie),	
	path('logout/',views.logout),
]
