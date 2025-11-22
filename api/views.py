from rest_framework.viewsets import ModelViewSet
from nhm_app.models import *
from .serializers import *

class DistrictViewSet(ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class GrantSchemeViewSet(ModelViewSet):
    queryset = GrantScheme.objects.all()
    serializer_class = GrantSchemeSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class MilestoneViewSet(ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer

class ExpenditureViewSet(ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer

class EvidenceViewSet(ModelViewSet):
    queryset = Evidence.objects.all()
    serializer_class = EvidenceSerializer

class AnomalyViewSet(ModelViewSet):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer