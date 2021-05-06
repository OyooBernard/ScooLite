from django.contrib import admin
from .models import Stream, Hostel, Title, Designation, TermYear, OpeningClosing

# Register your models here.
myModels = [Stream, Hostel, Title, Designation, TermYear, OpeningClosing]
admin.site.register(myModels)
