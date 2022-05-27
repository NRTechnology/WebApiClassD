from django.db import models

KELAMIN_CHOICES = [
    ('LK', 'Laki-Laki'),
    ('PR', 'Perempuan'),
]


# Create your models here.
class Mahasiswa(models.Model):
    Nim = models.CharField(max_length=10)
    Nama = models.CharField(max_length=255)
    TmpLahir = models.CharField(max_length=255)
    TglLahir = models.DateField()
    Alamat = models.CharField(max_length=255)
    Kelamin = models.CharField(max_length=2, choices=KELAMIN_CHOICES)
