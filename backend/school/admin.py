from django.contrib import admin
from .models import Student
from .models import Asignature
from .models import Notes
from .models import Teacher


# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Notes)
admin.site.register(Asignature)