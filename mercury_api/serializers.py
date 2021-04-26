from .models import Runner, Race, Result
from rest_framework import serializers

class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runner

        # showing all for now.
        fields = '__all__'
class RunnerResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Runner

        fields = ['id', 'first_name', 'last_name', 'city', 'state', 'real_time']


class ResultSerializer(serializers.ModelSerializer):

    # nesting all runners within a cohort
    runners = RunnerResultSerializer(source="runner", many=True)

    class Meta:
        model = Result

        # fields shown in output
        fields = ['cohort', 'runners']


class RaceSerializer(serializers.ModelSerializer):
    results = ResultSerializer(many=True)
    
    class Meta:
        model = Race

        # fields shown in output => showing all for now.
        fields = ['id', 'year', 'results']

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
