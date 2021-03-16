from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name="index"),
    path('api/profiles', views.ProfileListCreate.as_view(), name="profiles_lists")
]

