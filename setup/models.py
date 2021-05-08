from django.db import models

TERMS = (
    ('1', 'Term One'),
    ('2', 'Term Two'),
    ('3', 'Term three'),
)
YEARS = (
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
)
# Create your models here.
class Stream(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=10, unique=True) #abbreviation or short name

class Hostel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=10, unique=True)

class  Title(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbr = models.CharField(max_length=5, unique=True)

class Designation(models.Model):
    name = models.CharField(max_length=50, unique=True)

class TermYear(models.Model):
    term = models.CharField(max_length=1, choices=TERMS, unique=True)
    year = models.CharField(max_length=4, choices=YEARS, unique=True)
    
class OpeningClosing(models.Model):
    opening = models.DateField()
    closing = models.DateField()
    term = models.CharField(max_length=1, choices=TERMS)
    year = models.CharField(max_length=4, choices=YEARS)
   