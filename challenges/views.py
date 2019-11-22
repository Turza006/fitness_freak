from .models import Challenge,Overview,Workout,Diet

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ChallengeSerializer,DietSerializer,OverviewSerializer,WorkoutSerializer


class ChallengeListAPI(APIView):

    def get(self, request):

        challenge = Challenge.objects.all()

        json = ChallengeSerializer(data=challenge, many=True)
        json.is_valid()

        return Response(json.data, status=status.HTTP_200_OK)




class ChallengeCreateAPI(APIView):

    def post(self, request):

        params = request.data

        challenge_name = params.get('challenge_name', None)
        short_desc = params.get('short_desc', None)

        if challenge_name and short_desc:

            challenge = Challenge()
            challenge.challenge_name = challenge_name
            challenge.short_desc = short_desc
            challenge.save()

            res = {
                'Success': True,
                'UserId': id
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {
                'Success': False,
                'Reason': 'you are missing some required fields'
            }

            return Response(res, status=status.HTTP_400_BAD_REQUEST)


class DeleteChallengeAPI(APIView):

    def post(self, request):
        challenge_name = request.data.get('challenge_name', None)
        if challenge_name is None:
            res = {"Success": False, "Reason": "Id not found, you didn't give any id"}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        challenges = Challenge.objects.filter(challenge_name=challenge_name).all()
        if challenges.count() > 0:
            challenge = challenges[0]
            challenge.delete()

        res = {"Success": True}

        return Response(res, status=status.HTTP_200_OK)


class UpdateChallengeAPI(APIView):

    def post(self, request):
        challenge_name = request.data.get('challenge_name', None)
        challenges = Challenge.objects.filter(challenge_name=challenge_name).all()
        if challenges.count() > 0:
            challenge = challenges[0]

            data = request.data
            for key, value in data.items():
                challenge.__setattr__(key, value)
            challenge.save()
            res = {"Success": True, "Message": "User Data Updated"}
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {"Success": False, "Reason": "No user found with this id"}
            return Response(res, status=status.HTTP_200_OK)

