from django import forms

# class PatientForm(forms.Form):
#     AGE_CHOICES = [(i, str(i)) for i in range(18, 121)]  # Age options 18–120
#     age = forms.ChoiceField(choices=AGE_CHOICES, label="Age", widget=forms.Select(attrs={'class': 'form-select'}))
#     bmi = forms.FloatField(label="BMI", widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 0.1}))
#     smoker = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Smoker", widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     memory_problems = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Memory Problems", widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
#     family_history = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Family History", widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

class PatientForm(forms.Form):
    FunctionalAssessment = forms.FloatField(label="Functional Assessment")
    ADL = forms.FloatField(label="Activities of Daily Living (ADL)")
    MMSE = forms.FloatField(label="Mini-Mental State Examination (MMSE)")
    MemoryComplaints = forms.ChoiceField(
        label="Memory Complaints",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.RadioSelect
    )
    BehavioralProblems = forms.ChoiceField(
        label="Behavioral Problems",
        choices=[(0, "No"), (1, "Yes")],
        widget=forms.RadioSelect
    )
    BMI = forms.FloatField(label="Body Mass Index (BMI)")
    SleepQuality = forms.FloatField(label="Sleep Quality Score")
    PhysicalActivity = forms.FloatField(label="Physical Activity Level")
    CholesterolTriglycerides = forms.FloatField(label="Cholesterol Triglycerides Level")
    CholesterolHDL = forms.FloatField(label="Cholesterol HDL Level")
