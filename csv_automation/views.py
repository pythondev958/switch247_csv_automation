from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import TestRate, RatingPlan
from .serializers import TestRateSerializer, RatingPlanSerializer
from django.db.models import Max
from rest_framework.views import APIView
from rest_framework.response import Response

class TestRateViewSet(viewsets.ModelViewSet):
    queryset = TestRate.objects.all()
    serializer_class = TestRateSerializer

class RatingPlanViewSet(viewsets.ModelViewSet):
    queryset = RatingPlan.objects.all()
    serializer_class = RatingPlanSerializer



class MaxWeightRatingPlanView(APIView):
    def get(self, request, *args, **kwargs):
        max_weight = RatingPlan.objects.aggregate(Max('weight'))['weight__max']
        rating_plans = RatingPlan.objects.filter(weight=max_weight)
        serializer = RatingPlanSerializer(rating_plans, many=True)
        return Response(serializer.data) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    