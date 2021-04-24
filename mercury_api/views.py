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

# APIView tutorial: https://medium.com/the-andela-way/creating-a-django-api-using-django-rest-framework-apiview-b365dca53c1d
# class ResultByYearViewSet(viewsets.APIView):
#     # selectors from https://concisecoder.io/2018/12/23/how-to-optimize-your-django-rest-viewsets/
#     queryset = (
#         Results.objects.
#     ) 

    # def get(self, request):

