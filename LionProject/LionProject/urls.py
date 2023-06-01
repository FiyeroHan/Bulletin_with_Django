"""
URL configuration for LionProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from LionApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('modify_post/<int:pk>/', views.modify_post, name='modify_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('delete_reple/<int:reple_pk>/<int:post_pk>/', views.delete_reple, name='delete_reple')
]
