from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer


# Homepage
def home(request):
    return render(request, 'webApp/index.html')

class ProfileListCreate(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
