from django.forms import ModelForm, Textarea
from .models import TestItem


class TestItemForm (ModelForm):
    class Meta:
        model = TestItem
        fields = [
            'testName',
            'result',
            'flag',
            'reference',
        ]
        labels = {
            'testName' : '',
            'result' : '',
            'flag' : '',
            'reference' : '',
        }
        widgets = {
            'reference' : Textarea(attrs={'cols': 20, 'rows' : 5})
        }
