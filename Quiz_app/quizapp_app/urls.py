from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),
    path('signup/',views.signup  ,name='signup'),
    path('signin/',views.signin ,name='signin'),
    path('forgot_username/',views.forgot_username ,name='forgot_username'),
    path('forgot_otp/',views.forgot_otp  ,name='forgot_otp'),
    path('forgot_password/',views.forgot_password ,name='forgot_password'),
    path('deshboard/',views.deshboard  ,name='deshboard'),
    path('question/',views.question,name='question'),
    path('postdata/',views.postdata, name='postdata'),
    path('logout/',views.logout,name='logout'),
    path('result/',views.result1,name='result'),
    path('about/',views.about ,name='about'),
    path('contact/',views.contact ,name='contact'),

]
