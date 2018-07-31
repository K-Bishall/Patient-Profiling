from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.utils import timezone

from .forms import TestItemForm, SearchReportForm
from .models import User, TestItem

key = '00001'

# Create your views here.
def labReportInput(request):
    """Generate lab test input form"""

    testItemFormset = formset_factory(TestItemForm, extra=5)
    template = 'labtest.html'

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

datetest = timezone.now().date()

def labReportGenerate(request):
    """ Generates lab report in tabular form """

    template = 'labreport.html'

    #select * from TestItem where user_id = key and dateStamp = date
    testItems = TestItem.objects.filter(user_id = key, dateStamp = datetest)
    # print(testItems)

    #data to be rendered in template
    name = User.objects.get(pk=key).name
    date = datetest
    # print("name : ")
    # print(name)

    #list which contains all test records to be rendered
    testResult = []

    for test in testItems:
        #retrive information about the test record of patient
        testName = test.testName.testName
        result = test.result
        unit= test.testName.unit

        min = test.testName.minVal
        max = test.testName.maxVal
        reference = str(min) + '-' + str(max)
        
        if result > max:
            flag = 'H'
        elif result < min:
            flag = 'L'
        else:
            flag = ''
        
        testR = [testName, result, flag, unit, reference]
        testResult.append(testR)

    # print(testResult)

    return render(request, template, {
        'name': name,
        'date': date,
        'testResult': testResult,
    })

