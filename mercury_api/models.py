from django.db import models

# Create your models here.
class Runner(models.Model):

    ### Fields
    # Shown in queries
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    goal_time = models.DurationField()
    real_time = models.DurationField()

    # Not in queries
    email = models.EmailField(max_length=100)
    wheelchair = models.BooleanField(default=False)
    dob = models.DateField()
    sex = models.CharField(max_length=20)

    
# if only one field, maybe we shouldn't have it? stored in results
# HOWEVER! if we want to expand to different races around the world...
class Race(models.Model):
    year = models.IntegerField()
    # scalability: name, location (city/state/country)

### Junction table for M:n relationship
class Result(models.Model):
    # Race category e.g. age group + sex, determined in react
    cohort_id = models.PositiveIntegerField()

    runner = models.ForeignKey(
        Runner,                     # table name
        on_delete=models.RESTRICT,  # error out if trying to delete
        null=False)
        
    race_year = models.ForeignKey(
        Race,                       # table name
        on_delete=models.RESTRICT,  # error out if trying to delete
        null = False,              
        related_name='race')        # for db query