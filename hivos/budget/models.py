from django.db import models
from mastermodule.models import Common_Info
# Create your models here.

class Budget(Common_Info):
    ''' yearly plan model '''

    title = models.CharField(max_length=100, verbose_name='Title*')
    start_date = models.DateField('Start Date*')
    end_date = models.DateField('End Date*')
    budget = models.IntegerField('Budget*')
    description = models.TextField('Description')
    parent = models.ForeignKey('self', blank = True, null = True, related_name="budget_parent")
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.title

class Budget_Strategy(Common_Info):
    ''' strategy for budget '''

    title = models.CharField(max_length=100, verbose_name='Title*')
    budget = models.ForeignKey(Budget, verbose_name='Budget*')
    description = models.TextField('Descrition*')
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.title

class Activity_Status(Common_Info):
    name = models.CharField('Name*', max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

class Budget_Activity(Common_Info):
    ''' activity for budget '''

    title = models.CharField('Title*', max_length=100)
    budget = models.ForeignKey(Budget, verbose_name='Budget*')
    status = models.ForeignKey(Activity_Status, verbose_name='Status*')
    proposed_start_date = models.DateField(blank=True, null=True)
    proposed_end_date = models.DateField(blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    actual_end_date = models.DateField(blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    achivements = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.title
