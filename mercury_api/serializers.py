from .models import Runner, Race, Result
from rest_framework import serializers

class RunnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Runner

        # fields shown in output => showing all for now.
        exclude = ['url'];

class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race

        # fields shown in output => showing all for now.
        fields = '__all__';

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result

        # fields shown in output => showing all for now.
        fields = '__all__';