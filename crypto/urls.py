from django.urls import path
from crypto.views import *

urlpatterns = [
    path('', main, name='main'),
    path('post/<int:pk>', post)
]

