from django.contrib import admin
from django.urls import path
from centre import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('centre/teachers', views.index, name='index')
]
