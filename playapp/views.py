from rest_framework import generics

from .models import Plan
from .serializers import PlanSerializer


class QuotaPlanAPIView(generics.RetrieveAPIView):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
