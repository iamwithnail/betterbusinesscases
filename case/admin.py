from django.contrib import admin


# Register your models here.
from django.contrib import admin
from .models import Option, Score

admin.site.register(Option)
admin.site.register(Score)
