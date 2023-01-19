from django.shortcuts import render
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from tips.models import OverTwoAndHalf
from tips.serializers import OverSerializer

class OverViewset(viewsets.ModelViewSet):
    def get_queryset(self):
        # today = datetime.today()
        # datem = str(datetime(today.year, today.month, 1))
        # datem = datem.split(" ")[0]
        # range = self.request.query_params.get('date_range',None)
        hOver = self.request.query_params.get("home")
        aOver = self.request.query_params.get("away")
        if hOver is not None and aOver is not None:
            now = datetime.today()
            queryset = OverTwoAndHalf.objects.filter(home_over_percentage__gte = hOver, away_over_percentage__gte = aOver,startTime__gte=now)
            return queryset
        else:
            queryset = OverTwoAndHalf.objects.all()
            return queryset
    serializer_class = OverSerializer
        
               

 
