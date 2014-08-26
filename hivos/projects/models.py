from farmer.models import *
from hrmanagement.models import *
from finance.models import *
from events.models import *
#from training.models import *


class Activity_Status(Common_Info):
    name = models.CharField(max_length=100, verbose_name="Name*")
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name


class Coordinator_Type(Common_Info):
    name = models.CharField(max_length=100, verbose_name="Name*")
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

class Project_Type(Common_Info):
    name = models.CharField(max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

from farmer.models import Group, Farmer
class Project(Common_Info):
    project_type = models.ForeignKey(Project_Type, verbose_name="Project Type*")
    name = models.CharField(max_length=100, verbose_name='Name*')
    projectId = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    start_date = models.DateField('Start Date*', blank=True, null=True)
    end_date = models.DateField('End Date*', blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Budget*')
    status = models.ForeignKey(Activity_Status)
    project_coordinators = models.ManyToManyField(Staff, through='Project_Coordinators', blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True, null=True)
    members = models.ManyToManyField(Farmer, blank=True, null=True)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

    def get_project_hirarchy_for_training(self):

        content_type_obj = ContentType.objects.filter(name__iexact='project')
        hirarchy_list = ['project']
        milestone_list = Milestone.objects.filter(project=self)
        if milestone_list:
            hirarchy_list.append('milestone')

        return hirarchy_list

    def get_project_hirarchy_for_strategy(self):

        content_type_obj = ContentType.objects.filter(name__iexact='project')
        hirarchy_list = ['project']
        milestone_list = Milestone.objects.filter(project=self, active=2)
        if milestone_list:
            hirarchy_list.append('milestone')
        project_training_list = Training.objects.filter(content_type__model__iexact='project', object_id=self.id, active=2)
        if project_training_list:
            hirarchy_list.append('training')
        return hirarchy_list

    def get_project_hirarchy_for_activity(self):

        content_type_obj = ContentType.objects.filter(name__iexact='project')
        hirarchy_list = ['project']
        milestone_list = list(Milestone.objects.filter(project=self))
        if milestone_list:
            hirarchy_list.append('milestone')
        project_training_list = list(Training.objects.filter(content_type__model__iexact='project', object_id=self.id, active=2))
        if project_training_list:
            hirarchy_list.append('training')
        strategy_list1 = Strategy.objects.filter(content_type__model__iexact='project', object_id=self.id, active=2)
        milestone_ids = [i.id for i in milestone_list]
        strategy_list2 = Strategy.objects.filter(content_type__model__iexact='milestone', object_id__in=milestone_ids, active=2)
        training_ids = [i.id for i in project_training_list]
        strategy_list3 = Strategy.objects.filter(content_type__model__iexact='training', object_id__in=training_ids, active=2)
        if strategy_list1 or strategy_list2 or strategy_list3:
            hirarchy_list.append('strategy')

        return hirarchy_list


class Program(Common_Info):
    """ program can be training/event"""

    title = models.CharField(max_length=200, verbose_name='Title*')
    description = models.TextField(blank=True, null=True)
    venue = models.CharField(max_length=200)
    start_date = models.DateField('Start date*')
    end_date = models.DateField('End date*')
    batch_size = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    program_objective = models.TextField(blank=True, null=True)
    program_fees = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.title

class Milestone(Common_Info):
    project = models.ForeignKey(Project,verbose_name='Project*')
    title = models.CharField(max_length=200, verbose_name='Title*')
    description = models.TextField('Description*')
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.title

class Training(Common_Info):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    program = models.ForeignKey(Program, verbose_name='Program*')
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.program.title

    def get_object(self):
        if self.content_type.model == 'milestone':
            return Milestone.objects.get(id=self.object_id)


class Strategy(Common_Info):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    title = models.CharField(max_length=200, verbose_name='Title*')
    description = models.TextField('Description*')
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.title

    def get_object(self):
        if self.content_type.model == 'milestone':
            return Milestone.objects.get(id=self.object_id)
        elif self.content_type.model == 'training':
            return Training.objects.get(id=self.object_id)


class Project_Coordinators(Common_Info):
    project = models.ForeignKey(Project, related_name='Project_Cooridinators_Relation')
    staff = models.ForeignKey(Staff, verbose_name='Staff*')
    coordinator_type = models.ForeignKey(Coordinator_Type, verbose_name='Coordinator Type*')
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.staff

class Budget_Head(Common_Info):
    project = models.ForeignKey(Project, verbose_name='Project*')
    name = models.CharField(max_length=100, verbose_name='Name*')
    description = models.TextField(blank=True, null=True)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

class Activity_Type(Common_Info):
    name = models.CharField(max_length=100, verbose_name="Name*")
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

class Activity(Common_Info):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    budget_head = models.ForeignKey(Budget_Head, blank=True, null=True)
    title = models.CharField(max_length=200, verbose_name='Title*')
    activity_type = models.ForeignKey(Activity_Type, verbose_name='Activity Type*')
    description = models.TextField(blank=True, null=True)
    proposed_start_date = models.DateField(blank=True, null=True)
    proposed_end_date = models.DateField(blank=True, null=True)
    actual_start_date = models.DateField(blank=True, null=True)
    actual_end_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(Activity_Status, verbose_name='Status*')
    budget = models.DecimalField('Budget*', max_digits=10, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    challenges = models.TextField(blank=True, null=True)
    achivements = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.title

    def get_object(self):
        if self.content_type.model == 'milestone':
            return Milestone.objects.get(id=self.object_id)
        elif self.content_type.model == 'training':
            return Training.objects.get(id=self.object_id)
        elif self.content_type.model == 'strategy':
            return Strategy.objects.get(id=self.object_id)

