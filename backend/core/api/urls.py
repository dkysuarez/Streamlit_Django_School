from rest_framework.routers import DefaultRouter

from django.urls import path, include

from school.apiSchool.urls import student_router
from school.apiSchool.urls import asignature_router
from school.apiSchool.urls import notes_router
from school.apiSchool.urls import  teacher_router


router = DefaultRouter()


router.registry.extend(student_router.registry)
router.registry.extend(notes_router.registry)
router.registry.extend(asignature_router.registry)
router.registry.extend(teacher_router.registry)



urlpatterns = [
    path('',include(router.urls)),
]


