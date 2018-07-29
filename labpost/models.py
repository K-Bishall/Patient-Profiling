from django.db import models

# lab test record model
FLAG_CHOICE = [('N', 'Normal'), ('H', 'High'), ('L','Low'),]
class TestItem (models.Model):
    """This class is the actual record item
       to get the lab test."""

    id = models.AutoField(primary_key = True)
    testName = models.CharField(max_length=20)
    result = models.FloatField(default=0)
    flag = models.CharField(max_length = 1, choices = FLAG_CHOICE)
    reference = models.CharField(max_length = 20)

    def __str__(self):
        return self.testName
