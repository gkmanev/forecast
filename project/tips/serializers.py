from rest_framework import serializers
from datetime import datetime, timedelta, time
from tips.models import OverTwoAndHalf,Btts

class OverSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverTwoAndHalf
        fields = "__all__"
        
class BttsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Btts
        fields = "__all__"