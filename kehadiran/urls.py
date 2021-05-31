from django.contrib import admin
from django.urls import path, include


from homepage import views as homepage_views
from karyawan import views as karyawan_views
from kehadiran import views as kehadiran_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', karyawan_views.profil),
    path('login/', homepage_views.login_view),
    path('logout/', homepage_views.logout_view),
    path('daftar_hadir/', kehadiran_views.daftar_hadir),
    path('pengajuan_izin/', kehadiran_views.pengajuan_izin),
    path('daftar_izin/', kehadiran_views.daftar_izin),
]