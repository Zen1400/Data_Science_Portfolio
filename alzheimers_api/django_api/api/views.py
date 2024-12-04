from rest_framework.response import Response
from rest_framework.decorators import api_view
# from base.models import Item
# from .serializers import ItemSerializer
from .forms import PatientForm
from django.shortcuts import render, redirect
from .forms import PatientForm
from rest_framework.views import APIView
from .model.predict import predict_alzheimers
import pandas as pd
# import joblib
# import numpy as np
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# @api_view(["GET"])
# def getData(request):

#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)

#     return Response(serializer.data)


# # add data (sent from frontend) view and validate it
# @api_view(['POST', 'GET'])
# def addItem(request) :

#     serializer = ItemSerializer(data = request.data) # request.data : sent from the frontend

#     if serializer.is_valid() :   # validate same like validating forms
#         serializer.save() # create new item in the database

#     return Response(serializer.data)


# from django.shortcuts import render
# from .forms import PatientForm
# import joblib
# import numpy as np
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.compose import ColumnTransformer

# def patient_input(request):
#     result = None
#     if request.method == 'POST':
#         form = PatientForm(request.POST)
#         if form.is_valid():
#             # Extract form data
#             age = int(form.cleaned_data['age'])
#             bmi = form.cleaned_data['bmi']
#             smoker = int(form.cleaned_data['smoker'])
#             memory_problems = int(form.cleaned_data['memory_problems'])
#             family_history = int(form.cleaned_data['family_history'])

#             # Prepare data for prediction
#             data = [[age, bmi, smoker, memory_problems, family_history]]
#             result = data
#             # Redirect to the results page with the prediction
#             return redirect('result_page', result=result)
#     else:
#         form = PatientForm()

#     return render(request, 'patient_input.html', {'form': form, 'result': result})



def result_page(request, result):
    # Convert the result to an integer for rendering logic
    prediction = int(result)

    # Decide on the theme and image
    if prediction == 1:
        theme = {
            'message': "The patient is likely to have Alzheimer's.",
            'image': 'images/alzheimers_positive.jpg',
            'alert_class': 'alert-danger'
        }
    else:
        theme = {
            'message': "The patient is unlikely to have Alzheimer's.",
            'image': 'images/alzheimers_negative.jpg',
            'alert_class': 'alert-success'
        }

    return render(request, 'result.html', {'theme': theme})


# def predict_alzheimer(data):
#     # Load trained model
#     model = joblib.load('path/to/logistic_regression_model.pkl')
#     # Define preprocessor
#     preprocessor = ColumnTransformer(
#         transformers=[
#             ('scaler', StandardScaler(), [0, 1]),  # Scale age and bmi
#             ('encoder', OneHotEncoder(), [2, 3, 4])  # One-hot encode binary fields
#         ]
#     )
#     processed_data = preprocessor.fit_transform(data)
#     prediction = model.predict(processed_data)
#     return "Positive" if prediction[0] == 1 else "Negative"





from rest_framework import status
from .serializers import PatientInputSerializer

# class PatientInputAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = PatientInputSerializer(data=request.data)
#         if serializer.is_valid():
#             # Pass data to prediction function
#             result = predict_alzheimers() #serializer.validated_data)
#             return Response({"result": result}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientInputAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Render the HTML template for the user to input data
            form = PatientForm()
            return render(request, 'patient_input.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Handle the form submission
        serializer = PatientInputSerializer(data=request.POST)

        if serializer.is_valid():
            # Predict Alzheimer's using the validated data
            data = serializer.validated_data
            df = pd.DataFrame([data])  # Create a single-row DataFrame
            print(df)
            print(df.columns)
            print(df.dtypes)
            return predict_alzheimers(df)      #serializer.validated_data
            # return redirect('result_page', result=result)
            # return render(request, 'patient_input.html', {
            #     'form': serializer,
            #     'result': result,  # Pass the result to the template
            # })
        else:
            # Re-render the form with validation errors
            return render(request, 'patient_input.html', {
                'form': serializer,
                'errors': serializer.errors,
            })
