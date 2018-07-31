from django.forms import ModelForm, Textarea
from .models import TestItem
from django import forms


class TestItemForm (ModelForm):
    """ Form for adding lab records """
    class Meta:
        model = TestItem
        fields = [
            'testName',
            'result',
        ]
        labels = {
            'testName' : '',
            'result' : '',
        }

class SearchReportForm(forms.Form):
    """ Just a dummy form for selecting patient
    to generate report """
    userId = forms.CharField(max_length=5, label = 'Patient ID', help_text = 'Enter User ID')
    date = forms.DateField()

