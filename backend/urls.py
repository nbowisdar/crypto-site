from crypto.views import page404
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crypto.urls'))
]

handler404 = page404
