from django.contrib import admin
# from .models import Runner, Race, Result
from .models import Runner, Race

# Register your models here.
admin.site.register(Runner)
admin.site.register(Race)
# admin.site.register(Result)