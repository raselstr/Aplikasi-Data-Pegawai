# Generated by Django 3.2 on 2021-05-31 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
        ('kehadiran', '0003_auto_20210531_0838'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Izin',
            new_name='Izin1',
        ),
    ]