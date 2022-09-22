from django.shortcuts import render
from rest_framework import viewsets
from info_app.serializers import AboutUsSerializer, OurMissionSerializer, ContactSerializer, LogoSerializer
from info_app.models import AboutUs, Contact, OurMission, Logo


class AboutUsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class OurMissionViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = OurMission.objects.all()
    serializer_class = OurMissionSerializer


class ContactViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class LogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
