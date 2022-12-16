from django.urls import path
from . import views

urlpatterns=[
    path('appointments/',views.appointments,name='appointments'),
    path('appointments/<slug:aid>',views.modify_appointment,name='modify_appoint'),

    path('reception/',views.reception,name='reception'),
    path('setapt/',views.setapt,name='setapt'),
    path('setapt/<slug:pid>',views.setapt_pat,name='setapt_pat'),

    path('deletepat/',views.deletepat,name='deletepat'),
    path('updatepat/',views.updatepat,name='updatepat'),
    path('createpat/',views.createpat,name='crtpat'),
]