from django.forms import ModelForm, Textarea
from .models import TestItem
from django import forms


class TestItemForm (ModelForm):
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
