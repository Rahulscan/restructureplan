from rest_framework import generics

from .models import Plan
from .serializers import PlanSerializer


class QuotaPlanAPIView(generics.RetrieveAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

# class QuotaValueAPIView(generics.RetrieveAPIView):
#
#     def get(self, request, **kwargs):
#         try:
#             pk = kwargs.get('pk')
#             plan = Plan.objects.get(pk=pk)
#             quotas = plan.all_quotas
#             serializer = QuotaValueSerializer(quotas, many=True)
#             return Response(serializer.data)
#         except Plan.DoesNotExist:
#             return Response({"error": "Plan not found."}, status=404)
