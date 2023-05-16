from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name = "home"),
    path('about/', views.about,name = "about"),
    path('predictor/', views.predictor,name = "predictor"),
    path('contact/', views.contact,name="contact"),
    path('result/',views.result,name = "result"),
]
