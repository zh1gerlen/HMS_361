from django.urls import path
from . import views
urlpatterns=[
    path('addpres/',views.addpres,name='addpres'),
    path('addpres/<slug:pid>/',views.addpres_pat, name='addpres_pat'),

    path('showpres/',views.showpres,name='showpres'),
    path('showmedhis/',views.showmedhis,name='showmedhis'),
]