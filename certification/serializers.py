from rest_framework import serializers
from users.models import *
from certification.models import *

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certificate
        fields=['id','course_title_fani','code_fani','code_academy','certificate_image_academy','certificate_image_fani','fani_score','academy_score','online_course','course', 'user']





