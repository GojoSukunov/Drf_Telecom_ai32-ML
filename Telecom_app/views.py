from pathlib import Path

import joblib
from rest_framework.response import Response

from .serializers import TelecomSerializers
from rest_framework import views,status
from . import serializers


base_dir=Path(__file__).resolve().parent.parent

path_model=base_dir/'model'/'customers_model_ai32.pkl'
path_scaler=base_dir/'model'/'customers_scaler_ai32.pkl'

model=joblib.load(path_model)
scaler=joblib.load(path_scaler)


class TelecomViewSet(views.APIView):
    def post(self,request):
        instance=serializers.TelecomSerializers(data=self.request.data)
        if instance.is_valid():
            original_data=instance.validated_data.copy()
            new_data=instance.validated_data.copy()

            # 1. gender
            new_gender = new_data.pop('gender')
            gender_Male = [1 if new_gender == 'Male' else 0]

            # 2. Partner
            new_partner = new_data.pop('Partner')
            Partner_Yes = [1 if new_partner == 'Yes' else 0]

            # 3. Dependents
            new_dependents = new_data.pop('Dependents')
            Dependents_Yes = [1 if new_dependents == 'Yes' else 0]

            # 4. PhoneService
            new_phoneService = new_data.pop('PhoneService')
            PhoneService_Yes = [1 if new_phoneService == 'Yes' else 0]

            # 5. MultipleLines
            new_multipleLines = new_data.pop('MultipleLines')

            MultipleLines_phone_service_NO = [
                1 if new_multipleLines == 'No phone service' else 0
            ]

            MultipleLines_Yes = [
                1 if new_multipleLines == 'Yes' else 0
            ]

            # 6. InternetService
            new_internetService = new_data.pop('InternetService')

            InternetService_Fiber_optic = [
                1 if new_internetService == 'Fiber optic' else 0
            ]

            InternetService_No = [
                1 if new_internetService == 'No' else 0
            ]

            # 7. OnlineSecurity
            new_onlineSecurity = new_data.pop('OnlineSecurity')

            OnlineSecurity_internet_service_NO = [
                1 if new_onlineSecurity == 'No internet service' else 0
            ]

            OnlineSecurity_Yes = [
                1 if new_onlineSecurity == 'Yes' else 0
            ]

            # 8. OnlineBackup
            new_onlineBackup = new_data.pop('OnlineBackup')

            OnlineBackup_No_internet_service = [
                1 if new_onlineBackup == 'No internet service' else 0
            ]

            OnlineBackup_Yes = [
                1 if new_onlineBackup == 'Yes' else 0
            ]

            # 9. DeviceProtection
            new_deviceProtection = new_data.pop('DeviceProtection')

            DeviceProtection_No_internet_service = [
                1 if new_deviceProtection == 'No internet service' else 0
            ]

            DeviceProtection_Yes = [
                1 if new_deviceProtection == 'Yes' else 0
            ]

            # 10. TechSupport
            new_techSupport = new_data.pop('TechSupport')

            TechSupport_internet_service_NO = [
                1 if new_techSupport == 'No internet service' else 0
            ]

            TechSupport_Yes = [
                1 if new_techSupport == 'Yes' else 0
            ]

            # 11. StreamingTV
            new_streamingTV = new_data.pop('StreamingTV')

            StreamingTV_No_internet_service = [
                1 if new_streamingTV == 'No internet service' else 0
            ]

            StreamingTV_Yes = [
                1 if new_streamingTV == 'Yes' else 0
            ]

            # 12. StreamingMovies
            new_streamingMovies = new_data.pop('StreamingMovies')

            StreamingMovies_internet_service_NO = [
                1 if new_streamingMovies == 'No internet service' else 0
            ]

            StreamingMovies_Yes = [
                1 if new_streamingMovies == 'Yes' else 0
            ]

            # 13. Contract
            new_contract = new_data.pop('Contract')

            Contract_One_year = [
                1 if new_contract == 'One year' else 0
            ]

            Contract_Two_year = [
                1 if new_contract == 'Two year' else 0
            ]

            # 14. PaperlessBilling
            new_paperlessBilling = new_data.pop('PaperlessBilling')

            PaperlessBilling_Yes = [
                1 if new_paperlessBilling == 'Yes' else 0
            ]

            # 15. PaymentMethod
            new_paymentMethod = new_data.pop('PaymentMethod')

            PaymentMethod_Credit_card = [
                1 if new_paymentMethod == 'Credit card (automatic)' else 0
            ]

            PaymentMethod_Electronic_check = [
                1 if new_paymentMethod == 'Electronic check' else 0
            ]

            PaymentMethod_Mailed_check = [
                1 if new_paymentMethod == 'Mailed check' else 0
            ]

            features = ([
                            new_data ['SeniorCitizen'],
                            new_data ['tenure'],
                            new_data ['MonthlyCharges'],
                            new_data ['TotalCharges']
                        ] + gender_Male + Partner_Yes + Dependents_Yes + PhoneService_Yes
                        + MultipleLines_phone_service_NO + MultipleLines_Yes + InternetService_No + InternetService_Fiber_optic +
                        OnlineSecurity_internet_service_NO + OnlineSecurity_Yes + OnlineBackup_Yes + OnlineBackup_No_internet_service +
                        DeviceProtection_No_internet_service + DeviceProtection_Yes + TechSupport_internet_service_NO + TechSupport_Yes +
                        StreamingTV_Yes + StreamingTV_No_internet_service + StreamingMovies_Yes + StreamingMovies_internet_service_NO + Contract_One_year +
                        Contract_Two_year + PaperlessBilling_Yes + PaymentMethod_Credit_card + PaymentMethod_Mailed_check + PaymentMethod_Electronic_check)

            scaler_data = scaler.transform([features])
            prediction = int(model.predict(scaler_data)[0])
            telecom=instance.save(**original_data,prediction_telecom=prediction)
            return Response({'Prediction_Telecom':prediction,'data':TelecomSerializers(telecom).data},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)