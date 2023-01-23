from django.shortcuts import render
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from tips.models import OverTwoAndHalf, Btts
from tips.serializers import OverSerializer, BttsSerializer

class OverViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        hOver = self.request.query_params.get("home")
        aOver = self.request.query_params.get("away")
        print(hOver)
        if hOver is not None and aOver is not None:
            now = datetime.today()
            queryset = OverTwoAndHalf.objects.filter(home_over_percentage__gte = hOver, away_over_percentage__gte = aOver,startTime__gte=now)
            return queryset
        else:
            queryset = OverTwoAndHalf.objects.all()
            return queryset
    serializer_class = OverSerializer
        
               

class BttsViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        btts_home = self.request.query_params.get("btts_h")
        btts_away = self.request.query_params.get("btts_a")
        if btts_home is not None and btts_away is not None:
            now = datetime.today()
            queryset = Btts.objects.filter(btts_a__gte = btts_home, btts_b__gte = btts_away,startTime__gte=now)
            return queryset
        else:
            queryset = Btts.objects.all()
            return queryset
    serializer_class = BttsSerializer