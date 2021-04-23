from django.db import models

# Create your models here.
class Runner(models.Model):

    ### Dropdowns
    CHOICES_SEX = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    
    ### Fields
    first_name = models.Charfield(max_length=100)
    last_name = models.Charfield(max_length=100)
    city = models.Charfield(max_length=100)
    state = models.Charfield(max_length=100)
    country = models.Charfield(max_length=100)
    wheelchair = models.BooleanField(default=False)
    # TBD: dob, sex, goal_time

    ### Dropdown fields
    # sex = Models.CharField(max_length=2, choices=CHOICES_SEX)

# if only one field, maybe we shouldn't have it? stored in results
# HOWEVER! if we want to expand to different races around the world...
class Race(models.Model):
    year = models.IntegerField()
    # scalability: name, location (city/state/country)
    def __str__(self):
        return self.year

### Junction table for M:n relationship
class Result(models.Model):

     runner_id = models.ForeignKey(
        Runner,                     # table name
        on_delete=models.CASCADE,   # deep delete
        related_name='comments')    # 1 post => many comments

    race_year = models.ForeignKey(
        Race,                       # table name
        on_delete=models.CASCADE,   # deep delete
        related_name='comments')    # 1 post => many comments