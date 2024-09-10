from django.urls import path
from Webapp import views
urlpatterns = [
   
    path('', views.Index,name='index'),

]
