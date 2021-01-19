from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('add',views.addition, name='add'),
    path('verticalmoment' ,views.verticalmoment_load, name = 'vertical moment'),
    path('verticalmoment_calc' ,views.verticalmoment, name = 'vertical moment calc')
]