from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from .views import AsignatureViewSet
from .views import NotesViewSet
from .views import TeacherViewSet


student_router = DefaultRouter()

student_router.register(r'student', StudentViewSet)


teacher_router = DefaultRouter()

teacher_router.register(r'teacher', TeacherViewSet)


notes_router = DefaultRouter()

notes_router.register(r'notes', NotesViewSet)


asignature_router = DefaultRouter()

asignature_router.register(r'asignature', AsignatureViewSet)



