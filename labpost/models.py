from django.db import models

# lab test record model
class TestItem (models.Model):
    """This class is the actual record item
       to get the lab test."""

    id = models.AutoField(primary_key = True)
    testName = models.CharField(max_length=20)
    result = models.FloatField()
    flag = models.CharField(max_length = 1)
    reference = models.TextField(max_length = 100)

    def __str__(self):
        return self.testName
