from django.urls import path
from info_app.views import AboutUsViewSet, ContactViewsSet, OurMissionViewsSet, LogoViewSet


urlpatterns = [
    path('', AboutUsViewSet.as_view({'get': 'list'})),
    path('contact/', ContactViewsSet.as_view({'get': 'list'})),
    path('our-mission/', OurMissionViewsSet.as_view({'get': 'list'})),
    path('logo/', LogoViewSet.as_view({'get': 'list'})),
]
