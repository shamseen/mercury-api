from .models import Runner, Race, Result
from rest_framework import serializers

class RunnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Runner

        # showing all for now.
        # i have no idea where this url came from
        exclude = ['url'];

class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race

        # fields shown in output => showing all for now.
        fields = ['year'];

class ResultSerializer(serializers.ModelSerializer):
    # nesting all runners within a cohort
    runner = RunnerSerializer()

    class Meta:
        model = Result

        # fields shown in output
        fields = ('id', 'race_year', 'cohort_id', 'runner')

        ### Example JSON ###
        # [
        #     {
        #         "cohort_id": 1,
        #         "runners": [
        #         {
        #             "first_name": "Inge",
        #             "last_name": "Doey",
        #             "city": "Jamaica",
        #             "state": "New York",
        #             "time": "4:53:08"
        #         },
        #         {
        #             "first_name": "Nikolai",
        #             "last_name": "Shawl",
        #             "city": "Hartford",
        #             "state": "Connecticut",
        #             "time": "20:05:06"
        #         }
        #         ]
        #     },
        #     {
        #         "cohort_id": 2,
        #         "runners": [ ... ]
        #     },
        #     ...
        # ]
