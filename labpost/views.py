from django.shortcuts import render
from django.urls import reverse

from .forms import TestItemForm


# Create your views here.
def labReport(request):
    """Generate lab test report form"""

    if request.method == 'POST':
        pass

    else:
        return render(request,'template.html',{'form': TestItemForm})
