from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.utils import timezone

from .forms import TestItemForm
from .models import User, TestItem

key = '10003'

# Create your views here.
def labReport(request):
    """Generate lab test input form"""

    testItemFormset = formset_factory(TestItemForm, extra=5)
    template = 'template.html'

    testItemFormset = formset_factory(TestItemForm, extra=10)

    user = User.objects.get(pk = key)
    date = timezone.now().date()

    if request.method == 'POST':
        formset = testItemFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                length = len(form.cleaned_data)
                # print("form : " + str(length))
                # print("data : ")
                # print(form.cleaned_data)
                if length > 0 and form.is_valid():
                    test = form.save(commit=False)
                    test.user = User.objects.get(pk = key)
                    test.dateStamp = timezone.now().date()
                # print("form : " + str(length))
                # print("data : ")
                # print(form.cleaned_data)
                if length > 0 and form.is_valid():
                    test = form.save(commit=False)
                    test.user = user
                    test.dateStamp = date
                    test.save()

        return HttpResponseRedirect("")

    else:
        return render(request, template, {'formset': testItemFormset,'user': user, 'date': date,})
