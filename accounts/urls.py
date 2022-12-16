from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register,name="register"),
    path('login/',views.login,name='login'),
    path('uprofile',views.uprofile,name='uprofile'),
    path('profile',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('contactus/',views.contactus,name='contact'),
    path('list_patients/',views.list_patients,name='list_patients'),
    path('list_patients/<int:pk>',views.patient_detail,name='pat_detail'),
    path('<int:pk>',views.generate_pdf,name='generate_pdf'),
    path('list_patients/search/',views.search,name='search' ),


]