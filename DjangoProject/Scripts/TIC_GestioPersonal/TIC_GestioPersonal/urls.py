from django.contrib import admin
from django.urls import path
from centre import views # type: ignore

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('centre/teachers', views.teachers, name='teachers'),
    path('centre/students', views.students, name='students'),
    path('centre/form', views.form, name='form'),
]
