from rest_framework import serializers

from event_log.models import LogUserActivity

class LogUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogUserActivity
        fields = '__all__'