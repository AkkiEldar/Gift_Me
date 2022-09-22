from rest_framework import serializers
from info_app.models import AboutUs, Contact, OurMission, Logo


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class OurMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMission
        fields = '__all__'


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'
