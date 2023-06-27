from rest_framework import serializers

from playapp.models import Quota, Plan, PlanQuota


class QuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quota
        fields = ['codename', 'name', 'unit', 'description', 'is_boolean']


class PlanSerializer(serializers.ModelSerializer):
    quotas = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ['name', 'version', 'quotas', 'base_plan']

    def get_quotas(self, plan):
        return QuotaValueSerializer(plan.all_quotas, many=True).data


class QuotaValueSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='quota.name', read_only=True)

    class Meta:
        model = PlanQuota
        fields = ['name', 'value']
