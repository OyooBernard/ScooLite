from django import forms

#importing form models
from .models import Stream

class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = '__all__'
