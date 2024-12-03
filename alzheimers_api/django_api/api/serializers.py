from rest_framework import serializers
# from base.models import Item

# class ItemSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Item
#         fields = '__all__'


class PatientInputSerializer(serializers.Serializer):
    age = serializers.IntegerField(min_value=0, max_value=120, required=True)
    bmi = serializers.FloatField(min_value=0, required=True)
    smoker = serializers.BooleanField(required=True)
    memory_problems = serializers.BooleanField(required=True)
    family_history = serializers.CharField(max_length=100, required=True)
