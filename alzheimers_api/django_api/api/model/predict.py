import joblib
from django.shortcuts import render
import os


def predict_alzheimers(df) :
    model_path = os.path.join(os.path.dirname(__file__), 'random_forest.pkl')
    model = joblib.load(model_path)

    print("Model's expected features:", model.feature_names_in_)


    prediction = model.predict(df)

    if prediction == 1:
        # Theme for Alzheimer's
        return render(None, 'alz_theme.html', {"result": "Positive - Alzheimer detected"})
    else:
        # Theme for no Alzheimer's
        return render(None, 'no_alz_theme.html', {"result": "Negative - No Alzheimer detected"})
