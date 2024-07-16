from rest_framework import serializers

from ..models import Student
from ..models import Teacher
from ..models import Notes
from ..models import Asignature

from ..choices import GENDER_CHOICES

class GenderChoiceFiledSerializer(serializers.Field):
    def to_representation(self, obj):
        return dict(GENDER_CHOICES) [obj]

    def to_internal_value(self, data):
        return data


class StudentSerializers(serializers.ModelSerializer):
    gender = GenderChoiceFiledSerializer()
    enrolled = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = (
            'id',
            'name',
            'gender',
            'dateBth',
            'enrolled',
                )

    def get_enrolled(self, obj):
        return obj.enrolled.strftime('%Y-%m-%d %H:%M:%S')
    


class TeacherSerializers(serializers.ModelSerializer):
    gender = GenderChoiceFiledSerializer()
    class Meta:
        model = Teacher
        fields = (
            'id',
            'name',
            'gender',
            'phoneNumber',
            'emailAddress',
            'salary',
                )
        

class AsignatureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Asignature
        fields = (
            'id',
            'nameAsignature',
            'timeperClass',
                )


class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = (
            'id',
            'nameStudent',
            'nameTeacher',
            'nameAsignature',
            'note',
            )