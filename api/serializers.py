from rest_framework import serializers
from nhm_app.models import District, GrantScheme, Project, Milestone, Expenditure, Evidence, Anomaly

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['code','name']

class GrantSchemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrantScheme
        fields = ['id','scheme_name','total_amount']

class ProjectSerializer(serializers.ModelSerializer):
    district_name   = serializers.CharField(source='district.name', read_only=True)
    grant_name      = serializers.CharField(source='grant.scheme_name', read_only=True)
    spent_total     = serializers.SerializerMethodField()
    progress_pct    = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id','name','district_name','grant_name','allocated_amount','status','spent_total','progress_pct']

    def get_spent_total(self, obj):
        return obj.expenditure_set.aggregate(total=models.Sum('amount'))['total'] or 0

    def get_progress_pct(self, obj):
        return obj.milestone_set.filter(is_done=True).aggregate(s=models.Sum('weight'))['s'] or 0

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = ['id','project','task_name','weight','is_done']

class ExpenditureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenditure
        fields = ['id','project','amount','spent_date']

class EvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidence
        fields = ['id','project','file_url']

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = ['id','project','severity','message']