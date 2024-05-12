from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestRateViewSet, RatingPlanViewSet,MaxWeightRatingPlanView

router = DefaultRouter()
router.register(r'testrates', TestRateViewSet)
router.register(r'ratingplans', RatingPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/ratingplans/maxweight/', MaxWeightRatingPlanView.as_view(), name='max-weight-rating-plans'),

]














