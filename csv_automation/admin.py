

# Register your models here.
from django.contrib import admin
from .models import TestRate, RatingPlan

# Register your models here.
@admin.register(TestRate)
class TestRateAdmin(admin.ModelAdmin):
    list_display = ['rate_id', 'destination_id', 'rates_tag', 'rounding_method', 'rounding_decimals', 'max_cost', 'max_cost_strategy']
    search_fields = ['rate_id', 'destination_id']
    list_filter = ['rounding_method', 'max_cost_strategy']

@admin.register(RatingPlan)
class RatingPlanAdmin(admin.ModelAdmin):
    list_display = ['plan_id', 'destination_rates_id', 'timing_tag', 'weight']
    search_fields = ['plan_id', 'destination_rates_id']
    list_filter = ['timing_tag']