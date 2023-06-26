from django.urls import path
from . import views
from .views import QuotaPlanAPIView, QuotaValueAPIView

urlpatterns = [
    path('api/quota-plan/', QuotaPlanAPIView.as_view(), name='quota-plan-api'),
    path('api/quota-plan/<pk>/', QuotaPlanAPIView.as_view(), name='quota-plan-api'),
    path('plans/quotas/<int:pk>/', QuotaValueAPIView.as_view(), name='quota-value-api')
]
