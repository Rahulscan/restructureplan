from django.urls import path

from .views import QuotaPlanAPIView

urlpatterns = [
    path('plans/quotas/<pk>/', QuotaPlanAPIView.as_view(), name='quota-value-api')
]
