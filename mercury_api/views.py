from .models import Runner, Race, Result
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import RunnerSerializer, RaceSerializer, ResultSerializer
#GUI to test API without frontend built out

class RunnerViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Runner.objects.all()
    # The class used to serialize model
    serializer_class = RunnerSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]

class RaceViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Race.objects.all()
    # The class used to serialize model
    serializer_class = RaceSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]

class ResultViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Result.objects.all()
    # The class used to serialize model
    serializer_class = ResultSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny]