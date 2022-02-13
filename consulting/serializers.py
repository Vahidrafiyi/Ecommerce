from consulting.models import ConsultationForm
from rest_framework import serializers

class ConsultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationForm
        fields = '__all__'