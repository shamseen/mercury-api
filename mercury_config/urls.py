from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mercury_api.views import RunnerViewSet, RaceViewSet, ResultViewSet

# create a new router
router = routers.DefaultRouter()

# register viewsets/endpoint GUI
router.register(r'api', RunnerViewSet) #register/api routes


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]