from django.db import models


OPTION_TYPES = (
            ('scale', 'Scale and Scope'),
            ('delivery', 'Delivery approaches'),
            ('speed', 'Speed of Delivery'),
            ('fourth', 'Fourth Option'),
            ('fifth', 'Fifth Option'))

STRENGTH = (
    ('basic', 'Baseline, do-nothing option'),
    ('min', 'Minimum option'),
    ('inter', 'Intermediate option'),
    ('ambit', 'Ambitious, full option')
)

FACTOR_CHOICES = (
    ('vfm', 'Value for Money'),
    ('cst', 'Immediate affordability'),
    ('fit', 'Strategic Fit'),
    ('ach', 'Achievability'),
    ('csf', 'Critical Success Factors')
)
class Option(models.Model):
    option_type = models.CharField(max_length=8, choices=OPTION_TYPES)
    strength = models.CharField(max_length=5, choices=STRENGTH)
    text = models.TextField()

class Score(models.Model):
    option = models.ForeignKey(Option)
    factor = models.TextField(max_length=5, choices=FACTOR_CHOICES)
    score = models.PositiveIntegerField(max_length=1)