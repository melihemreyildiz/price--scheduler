from django.contrib import admin
from django.urls import path, include
from project.jobs import *

start()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('project.urls'))
]

