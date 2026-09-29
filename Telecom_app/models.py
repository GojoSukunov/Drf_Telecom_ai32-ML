from django.db import models

class TelecomPrediction(models.Model):
    SeniorCitizen=models.PositiveSmallIntegerField(default=0)
    tenure=models.PositiveSmallIntegerField(default=0)
    MonthlyCharges=models.PositiveSmallIntegerField(default=0)
    TotalCharges=models.PositiveSmallIntegerField(default=0)
    gender=models.CharField(max_length=32)
    Partner=models.CharField(max_length=32)
    Dependents=models.CharField(max_length=32)
    PhoneService=models.CharField(max_length=32)
    MultipleLines=models.CharField(max_length=32)
    InternetService=models.CharField(max_length=32)
    OnlineSecurity=models.CharField(max_length=32)
    OnlineBackup=models.CharField(max_length=32)
    DeviceProtection=models.CharField(max_length=32)
    TechSupport=models.CharField(max_length=32)
    StreamingTV=models.CharField(max_length=32)
    StreamingMovies=models.CharField(max_length=32)
    Contract=models.CharField(max_length=32)
    PaperlessBilling=models.CharField(max_length=32)
    PaymentMethod=models.CharField(max_length=32)

    prediction_telecom=models.CharField(max_length=32)