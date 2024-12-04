from rest_framework import serializers
# from base.models import Item

# class ItemSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Item
#         fields = '__all__'




class PatientInputSerializer(serializers.Serializer):
    FunctionalAssessment = serializers.FloatField()
    ADL = serializers.FloatField()
    MMSE = serializers.FloatField()
    MemoryComplaints = serializers.IntegerField()  # Binary: 0 or 1
    BehavioralProblems = serializers.IntegerField()  # Binary: 0 or 1
    BMI = serializers.FloatField()
    SleepQuality = serializers.FloatField()
    PhysicalActivity = serializers.FloatField()
    CholesterolTriglycerides = serializers.FloatField()
    CholesterolHDL = serializers.FloatField()
