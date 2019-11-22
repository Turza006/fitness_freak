from rest_framework.serializers import ModelSerializer

from .models import Challenge,Overview,Workout,Diet


class ChallengeSerializer(ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'


class OverviewSerializer(ModelSerializer):
    class Meta:
        model = Overview
        fields = '__all__'
class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class DietSerializer(ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'