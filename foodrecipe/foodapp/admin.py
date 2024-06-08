from django.contrib import admin

from foodapp.models import *

# Register your models here.
admin.site.register(Food)

def __str__(self):
        return self.user.name