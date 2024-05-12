from django.db import models

from django.db import models

class TestRate(models.Model):
    rate_id = models.CharField(max_length=40, blank=True, null=True)  # Renamed from 'id' to 'rate_id'
    destination_id = models.CharField(max_length=40, blank=True, null=True)
    rates_tag = models.CharField(max_length=40, blank=True, null=True)
    rounding_method = models.CharField(max_length=40, blank=True, null=True)
    rounding_decimals = models.CharField(max_length=40, blank=True, null=True)
    max_cost = models.CharField(max_length=40, blank=True, null=True)
    max_cost_strategy = models.CharField(max_length=40, blank=True, null=True)

class RatingPlan(models.Model):
    plan_id = models.CharField(max_length=40, blank=True, null=True)  # Renamed from 'id' to 'plan_id'
    destination_rates_id = models.CharField(max_length=40, blank=True, null=True)
    timing_tag = models.CharField(max_length=40, blank=True, null=True)
    weight = models.CharField(max_length=40, blank=True, null=True)

# class TestRate(models.Model):
#     id = models.CharField(max_length=40, primary_key=False)
#     # id = models.CharField(max_length=40, primary_key=True)

#     destination_id = models.CharField(max_length=40, blank=True, null=True)
#     rates_tag = models.CharField(max_length=40, blank=True, null=True)
#     rounding_method = models.CharField(max_length=40, blank=True, null=True)
#     rounding_decimals = models.CharField(max_length=40, blank=True, null=True)
#     max_cost = models.CharField(max_length=40, blank=True, null=True)
#     max_cost_strategy = models.CharField(max_length=40, blank=True, null=True)

# class RatingPlan(models.Model):
#     id = models.CharField(max_length=40, primary_key=False)
#     # id = models.CharField(max_length=40, primary_key=True)

#     destination_rates_id = models.CharField(max_length=40, blank=True, null=True)
#     timing_tag = models.CharField(max_length=40, blank=True, null=True)
#     weight = models.CharField(max_length=40, blank=True, null=True)
    
    
    
    
    
    
    
    
    
    
    
    