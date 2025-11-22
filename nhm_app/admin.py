from django.contrib import admin
from .models import *

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('code','name')

@admin.register(GrantScheme)
class GrantSchemeAdmin(admin.ModelAdmin):
    list_display = ('scheme_name','total_amount')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','district','allocated_amount','status')

@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('project','task_name','weight','is_done')
    list_filter  = ('project',)

@admin.register(Expenditure)
class ExpenditureAdmin(admin.ModelAdmin):
    list_display = ('project','amount','spent_date')

@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    list_display = ('project','file_url')

@admin.register(Anomaly)
class AnomalyAdmin(admin.ModelAdmin):
    list_display = ('project','severity','message')
    list_filter  = ('severity',)