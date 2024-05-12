
from rest_framework import serializers
from .models import TestRate, RatingPlan

class TestRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestRate
        fields = ['id', 'destination_id', 'rates_tag', 'rounding_method', 'rounding_decimals', 'max_cost', 'max_cost_strategy']
        extra_kwargs = {field: {'allow_null': True, 'required': False} for field in fields}

class RatingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingPlan
        fields = ['id', 'destination_rates_id', 'timing_tag', 'weight']
        extra_kwargs = {field: {'allow_null': True, 'required': False} for field in fields}
 
        
        
        
        
        
        
        