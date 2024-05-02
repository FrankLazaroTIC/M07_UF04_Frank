from django.contrib import admin
from django.urls import path
from centre import views # type: ignore

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.llistarUsersIndex, name='index'),
    path('centre/teachers', views.llistarProfessors, name='teachers'),
    path('centre/students', views.llistarUsers, name='students'),
    path('centre/form', views.form, name='form'),
    path('centre/update/<int:id>', views.updateUser, name='updateUser'),
    path('centre/delete/<int:id>', views.deleteUser, name='deleteUser'),
]
