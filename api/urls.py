from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('districts', DistrictViewSet)
router.register('grants', GrantSchemeViewSet)
router.register('projects', ProjectViewSet)
router.register('milestones', MilestoneViewSet)
router.register('expenditures', ExpenditureViewSet)
router.register('evidences', EvidenceViewSet)
router.register('anomalies', AnomalyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]