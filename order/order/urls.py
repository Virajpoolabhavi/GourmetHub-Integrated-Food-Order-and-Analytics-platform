"""
URL configuration for order project.

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
from order import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('',views.homepage),
    path('reg_save/',views.reg_save,name='reg_save'),
    path('login_save/',views.login_save,name='login_save'),
    path('menu/',views.menu,name='menu'),
    path('order/',views.order,name='order'),
    path('order_summary/',views.order_summary,name='order_summary'),
    path('add/',views.add,name='add'),
    path('dash/',views.dash,name='dash'),
    path('cdash/',views.cdash,name='cdash'),
] + static( settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
