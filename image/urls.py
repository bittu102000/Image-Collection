from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home,name="home"),
    path('category/<int:id>/',views.category,name='category'),
    
]