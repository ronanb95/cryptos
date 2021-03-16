#SIDE NOTE: Ideally would have made new app for the profile section but due to time and small size I am assuming it is fine to keep this project to single app
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField(read_only=True)
    email = serializers.SerializerMethodField(read_only=True)
    
    #Override: Want username instead of integer number for user
    def get_user(self, obj):
        # obj is model instance
        return obj.user.username

    #Override: Want username instead of integer number for user
    def get_email(self, obj):
        # obj is model instance
        return obj.user.email

    class Meta:
	    model = Profile
	    fields = ('user','image','fav_coin','email')