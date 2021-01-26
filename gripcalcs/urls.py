from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.addition, name='add'),
    path('verticalmoment' ,views.verticalmoment_load, name = 'vertical moment'),
    path('verticalmoment_calc' ,views.verticalmoment, name = 'vertical moment calc'),
    path('torquetoforce', views.torquetoforce, name = 'torque to force')
    #path('Torquetoforce_calc', views.Torquetoforce_calc, name = 'torque to force calc')
]