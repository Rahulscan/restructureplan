from django.contrib import admin
from .models import Quota, Plan, PlanQuota


@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_display = ['codename', 'name', 'is_boolean']


class QuotaInline(admin.StackedInline):
    model = PlanQuota
    extra = 1
    fields = ['quota', 'value']


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'version']
    inlines = [QuotaInline]
