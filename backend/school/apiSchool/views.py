from rest_framework import viewsets

from .serializers import StudentSerializers
from .serializers import NotesSerializers
from .serializers import AsignatureSerializers
from .serializers import TeacherSerializers


from ..models import Student
from ..models import Asignature
from ..models import Notes
from ..models import Teacher




class StudentViewSet(viewsets.ModelViewSet):
    queryset =  Student.objects.all()
    serializer_class = StudentSerializers

class NotesViewSet(viewsets.ModelViewSet):
    queryset =  Notes.objects.all()
    serializer_class = NotesSerializers

class AsignatureViewSet(viewsets.ModelViewSet):
    queryset =  Asignature.objects.all()
    serializer_class = AsignatureSerializers


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

