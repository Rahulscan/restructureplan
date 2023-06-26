from itertools import chain

from rest_framework.response import Response
from .models import Plan
from .serializers import PlanSerializer, QuotaValueSerializer
from rest_framework import generics


class QuotaPlanAPIView(generics.RetrieveAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()


class QuotaValueAPIView(generics.RetrieveAPIView):
    def get(self, request, pk):
        try:
            plan = Plan.objects.get(pk=pk)
            quotas = plan.all_quotas
            serializer = QuotaValueSerializer(quotas, many=True)
            return Response(serializer.data)
        except Plan.DoesNotExist:
            return Response({"error": "Plan not found."}, status=404)




