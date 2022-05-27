from django.contrib import admin
from .models import Mahasiswa


class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('Nim', 'Nama')


# Register your models here.
admin.site.register(Mahasiswa, MahasiswaAdmin)
