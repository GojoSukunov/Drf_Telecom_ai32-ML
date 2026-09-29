from django.urls import path
from .views import TelecomViewSet

urlpatterns=[
    path('telecom_prediction',TelecomViewSet.as_view(),name='telecom-prediction')
]