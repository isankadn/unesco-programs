from django.urls import path
from django.shortcuts import render
from django.core.exceptions import PermissionDenied

from . import views


def permission_denied_view(request, exception=None):
    return render(request, 'permission_denied.html', status=403)


urlpatterns = [
    path('', views.program_list, name='program_list'),
    path('add/', views.add_program, name='add_program'),
    path('<slug:program_slug>/edit/', views.edit_program, name='edit_program'),
    path('<slug:program_slug>/', views.program_detail, name='program_detail'),    
    
]

handler403 = permission_denied_view