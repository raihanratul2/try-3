from django.urls import path
from .views import *
urlpatterns = [
    path('',First,name='First',),
    path('update/',update,name='update',),
    path('create2/',create2,name='create2',),
] 





