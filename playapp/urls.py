from django.urls import path

from .views import QuotaValueAPIView

urlpatterns = [
    path('plans/quotas/<int:pk>/', QuotaValueAPIView.as_view(), name='quota-value-api')
]
