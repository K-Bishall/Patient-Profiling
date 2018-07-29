from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import formset_factory

from .forms import TestItemForm


# Create your views here.
def labReport(request):
    """Generate lab test report form"""

    testItemFormset = formset_factory(TestItemForm, extra=2)

    # if request.method == 'POST':
    #     testItem = TestItemForm(request.POST)

    #     if testItem.is_valid():
    #         testItem.save()

    #     return HttpResponseRedirect("")

    # if request.method == 'POST':
    #     formset = testItemFormset(request.POST)
    #     if formset.is_valid():
    #         # formset = formset.cleaned_data
    #         for test in formset:
    #             if test.has_changed():
    #                 test.save()

    #     return HttpResponseRedirect("")

    if request.method == 'POST':
        formset = testItemFormset(request.POST)
        if formset.is_valid():
            for test in formset:
                data = test.cleaned_data
                flag = True
                for _, value in data:
                    if value == '':
                        flag = False
                        break
                if flag:
                    test.save()

        return HttpResponseRedirect("")

    else:
        return render(request, 'template.html', {'formset': testItemFormset,})
