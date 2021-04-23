from django.db import models

# Create your models here.
class Runner(models.Model):
    
    ### Fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    wheelchair = models.BooleanField(default=False)
    goal_time = models.DurationField()
    real_time = models.DurationField()
    dob = models.DateField()
    sex = models.CharField(max_length=20)

# if only one field, maybe we shouldn't have it? stored in results
# HOWEVER! if we want to expand to different races around the world...
class Race(models.Model):
    year = models.IntegerField()
    # scalability: name, location (city/state/country)
    def __str__(self):
        return self.year

### Junction table for M:n relationship
class Result(models.Model):
    # Race category e.g. age group + sex
    cohort = models.PositiveIntegerField()

    runner_id = models.ForeignKey(
        Runner,                     # table name
        on_delete=models.RESTRICT,  # error out if trying to delete
        null=False,
        related_name='+')           # can't be called by Runner operations
        
    race_year = models.ForeignKey(
        Race,                       # table name
        on_delete=models.RESTRICT,  # error out if trying to delete
        null = False,              
        related_name='+')           # can't be called by Race operations