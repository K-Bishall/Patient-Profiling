from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import TestItemForm
from django.forms import formset_factory


# Create your views here.
def labReport(request):
    """Generate lab test report form"""

    if request.method == 'POST':
        testItem = TestItemForm(request.POST)

        if testItem.is_valid():
            # testItem = testItem.cleaned_data
            testItem.save()

            return HttpResponseRedirect("")


    else:
        return render(request,'template.html',{'form': TestItemForm})
