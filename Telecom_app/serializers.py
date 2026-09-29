from .models import TelecomPrediction
from rest_framework import serializers


class TelecomSerializers(serializers.ModelSerializer):
    class Meta:
        model=TelecomPrediction
        fields=['SeniorCitizen','tenure','MonthlyCharges','TotalCharges','gender','Partner','Dependents','PhoneService','MultipleLines',
                'InternetService','OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies','Contract',
                'PaperlessBilling','PaymentMethod']