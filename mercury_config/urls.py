from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from mercury_api.views import RunnerViewSet, RaceViewSet, ResultViewSet
from mercury_api.views import RunnerViewSet, RaceViewSet

# create a new router
router = routers.DefaultRouter()

# register viewsets/endpoint GUI
router.register(r'runner', RunnerViewSet) #get all runners routes
# router.register(r'result', ResultViewSet)
router.register(r'race', RaceViewSet)


urlpatterns = [
    # add all of our router urls
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]