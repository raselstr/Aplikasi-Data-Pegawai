from __future__ import unicode_literals
from mywebsite.settings import TIME_ZONE
from django.db import models

from karyawan.models import Karyawan


# Create your models here.

class Kehadiran(models.Model):
    JENIS_KEHADIRAN_CHOICES = (
        ('izin', 'Izin'),
        ('cuti', 'Cuti'),
        ('alpa', 'Tanpa Alasan'),
        ('hadir', 'Hadir'),
    )
    karyawan = models.ForeignKey(Karyawan, on_delete=models.CASCADE, null=True)
    jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICES, default='hadir')
    waktu = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.karyawan.nama

class Izin1(models.Model):
    JENIS_KEHADIRAN_CHOICES = (
        ('izin', 'Izin'),
        ('cuti', 'Cuti')
    )

    karyawan = models.ForeignKey(Karyawan,on_delete=models.CASCADE, null=True)
    jenis_kehadiran = models.CharField(max_length=20, choices=JENIS_KEHADIRAN_CHOICES)
    waktu_mulai = models.DateField()
    waktu_berhenti = models.DateField()
    alasan = models.TextField()
    disetujui = models.BooleanField(default=False)

    def __unicode__(self):
        return self.karyawan.nama