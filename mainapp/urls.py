from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index),
    path('create/', views.create_link, name='create_link'),
    path("<int:targetid>/",  views.redirect_to_matching, name="view"),
    path("<int:targetid>/overview/", views.overview_of_shortener, name="overview"),
]
