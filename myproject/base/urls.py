from django.urls import path
from base import views

urlpatterns=[
    path('create_destination/',views.create_destination, name='create_destination'),
    path('destination_list/',views.destination_list, name='destination_list'),
    path('addactivity/',views.addactivity, name='addactivity'),
    path('allactivity/',views.allactivity, name='allactivity'),
    path('activityofeachdest/<int:did>',views.activityofeachdest, name='activityofeachdest'),
    path('destread/<int:did>/',views.destread,name='destread'),
    path('actread/<int:aid>/',views.actread,name='actread'),
    path('actupdate/<int:pid>',views.actupdate, name='actupdate'),
    path('actdelete/<int:pid>',views.actdelete, name='actdelete'),
    path('acthistory',views.acthistory, name='acthistory'),
    path('actrestore/<int:pid>',views.actrestore, name='actrestore'),
    path('actdeleteperm/<int:pid>',views.actdeleteperm, name='actdeleteperm'),


]