__author__ = 'chris'

from django import forms

from .models import Option

class OptionForm(forms.ModelForm):

    class Meta:
        model = Option
        fields = ('option_type', 'strength', 'text',)
