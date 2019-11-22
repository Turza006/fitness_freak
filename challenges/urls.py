from django.urls import path

from .views import ChallengeListAPI,DeleteChallengeAPI,UpdateChallengeAPI,ChallengeCreateAPI

urlpatterns = [
    path('', ChallengeListAPI.as_view(), name='Challenge List'),
    path('create', ChallengeCreateAPI.as_view(), name='CreateChallengeAPI'),
    path('delete', DeleteChallengeAPI.as_view(), name='Delete Challenge API'),
    path('update', UpdateChallengeAPI.as_view(), name='Update Challenge API'),

]
