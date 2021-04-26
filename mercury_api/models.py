from django.db import models

# Create your models here.
class Runner(models.Model):

    ### Fields
    # Shown in results table
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    real_time = models.DurationField(null=True)

    # Not in results table
    # goal_time = models.DurationField() # messing with form POST
    email = models.EmailField(max_length=100)
    wheelchair = models.BooleanField(default=False)
    dob = models.DateField()
    sex = models.CharField(max_length=20)

    
# if only one field, maybe we shouldn't have it? stored in results
# HOWEVER! if we want to expand to different races around the world...
class Race(models.Model):
    year = models.PositiveIntegerField()
    # scalability: name, location (city/state/country)

### Junction table for M:n relationship
class Result(models.Model):
    # Race category e.g. age group + sex, determined in react
    cohort = models.PositiveIntegerField()

    # Will show a nested array of runner objs
    runner = models.ManyToManyField(Runner)
        
    race = models.ForeignKey(
        Race,                       # table name
        on_delete=models.RESTRICT,  # error out if trying to delete
        null = False,              
        related_name='results')     # for db query