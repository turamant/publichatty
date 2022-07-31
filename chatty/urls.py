from django.urls import path

from chatty import views

urlpatterns = [
    path('', views.index)
]