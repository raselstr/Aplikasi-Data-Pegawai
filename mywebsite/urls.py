"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include

from homepage import views as homepage_views
from karyawan import views as karyawan_views
from kehadiran import views as kehadiran_views

urlpatterns = [
    # path('pegawai/',include('pegawai.urls')),
    path('admin/', admin.site.urls),
    path('',karyawan_views.profil),
    path('login/', homepage_views.login_view),
    path('logout/', homepage_views.logout_view),
    path('daftar_hadir/', kehadiran_views.daftar_hadir),

]
