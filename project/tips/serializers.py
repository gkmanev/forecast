from rest_framework import serializers
from datetime import datetime, timedelta, time
from tips.models import OverTwoAndHalf

class OverSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverTwoAndHalf
        fields = "__all__"