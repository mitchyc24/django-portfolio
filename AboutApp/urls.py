from django.urls import path
from . import views


# #######:8000/about
urlpatterns = [path('',views.about_view)]