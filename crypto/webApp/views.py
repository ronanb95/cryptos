from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
import json
import requests


# Homepage
def home(request):
    return render(request, 'webApp/index.html')

# Creates the API to retrieve profile data
class ProfileListCreate(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

# Gets realtime data
# Obviously cause issues with multiple concurrent users
# Possible Solution: Log this data to database every 5 minutes or so and retrieve from there 
class RealTimeInfoView(generics.RetrieveAPIView):
    
    queryset=''

    def get(self, request):

        api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=eur&order=market_cap_desc&per_page=300&page=1&sparkline=false&price_change_percentage=24h"

        try:
            res = requests.get(api_url)
        except Exception as e:
            error_data = "Error, problem with real time URL: " + e
            return Response(error_data, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        json_resp = json.loads(res.text)

        return Response(json_resp, status=status.HTTP_200_OK)