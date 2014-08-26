from projects.models import *
from django import forms


class Activity_Status_Form(forms.ModelForm):
    class Meta:
        model = Activity_Status
        exclude = ('created_on', 'active')

class Coordinator_Type_Form(forms.ModelForm):
    class Meta:
        model = Coordinator_Type
        exclude = ('created_on', 'active')

class Project_Type_Form(forms.ModelForm):
    class Meta:
        model = Project_Type
        exclude = ('created_on', 'active')

class Activity_Type_Form(forms.ModelForm):
    class Meta:
        model = Activity_Type
        exclude = ('created_on', 'active')

class Project_Form(forms.ModelForm):

    project_type_list = Project_Type.objects.filter(active=2)
    activity_status_list = Activity_Status.objects.filter(active=2)
    project_type = forms.ModelChoiceField(queryset=project_type_list, label='Project Type*')
    status = forms.ModelChoiceField(queryset=activity_status_list, label='Status*')
    class Meta:
        model = Project
        exclude = ('created_on', 'active', 'project_coordinators', 'members')

class Project_Coordinator_Form(forms.ModelForm):
    class Meta:
        model = Project_Coordinators
        exclude = ('created_on', 'active')

class Budget_Head_Form(forms.ModelForm):
    class Meta:
        model = Budget_Head
        exclude = ('created_on', 'active')

class Milestone_Form(forms.ModelForm):

    class Meta:
        model = Milestone
        exclude = ('created_on', 'active', 'project')

def Project_Training_Form(project_id):

    class cus_project_training_form(forms.Form):

        project_list = Project.objects.filter(id=int(project_id))
        milestone_list = Milestone.objects.filter(project=project_list[0],active=2)
        hirarchy_list = project_list[0].get_project_hirarchy_for_training()
        hirarchy_tuple = tuple(zip(hirarchy_list, hirarchy_list))

        #project = forms.ModelChoiceField(queryset=project_list, initial={'project':project_list[0]})
        training_for = forms.ChoiceField(choices=hirarchy_tuple)
        milestone = forms.ModelChoiceField(queryset=milestone_list, required=False)
        training_title = forms.CharField(max_length=100,label='Training Title*')
        description = forms.CharField(widget=forms.Textarea, required=False)
        venue = forms.CharField(widget=forms.Textarea, label='Venue')
        start_date = forms.DateField(label='Start Date*', input_formats=['%Y-%m-%d'])
        end_date = forms.DateField(label='End Date*', input_formats=['%Y-%m-%d'])
        batch_size = forms.CharField(max_length=100, required=False)
        language = forms.CharField(max_length=100, required=False)
        program_objective = forms.CharField(widget=forms.Textarea, required=False)
        program_fees = forms.CharField(max_length=100, required=False)

    return cus_project_training_form

def Stretegy_Form(project_id):

    class cus_strategy_form(forms.ModelForm):

        project_list = Project.objects.filter(id=int(project_id))
        milestone_list = Milestone.objects.filter(project=project_list[0], active=2)
        hirarchy_list = project_list[0].get_project_hirarchy_for_strategy()
        training_list = Training.objects.all() # initially anything,as its hidden in form and on selecting milestone getting objects according to milestone using ajax
        hirarchy_tuple = tuple(zip(hirarchy_list, hirarchy_list))

        #project = forms.ModelChoiceField(queryset=project_list, initial={'project':project_list[0]})
        strategy_for = forms.ChoiceField(choices=hirarchy_tuple, label='Strategy For*')
        milestone = forms.ModelChoiceField(queryset=milestone_list, required=False)
        training = forms.ModelChoiceField(queryset=training_list, required=False)

        class Meta:
            model = Strategy
            fields = ['title', 'strategy_for', 'milestone', 'training', 'description']
    return cus_strategy_form

def Activity_Form(project_id):

    class cus_activity_form(forms.ModelForm):

        project_list = Project.objects.filter(id=int(project_id))
        milestone_list = Milestone.objects.filter(project=project_list[0], active=2)
        hirarchy_list = project_list[0].get_project_hirarchy_for_activity()
        training_list = Training.objects.all() # initially anything,as its hidden in template and on selecting milestone getting objects according to milestone using ajax
        strategy_list = Strategy.objects.all() # initially anything,as its hidden in template and on selecting training getting objects according to training using ajax
        hirarchy_tuple = tuple(zip(hirarchy_list, hirarchy_list))

        #project = forms.ModelChoiceField(queryset=project_list, initial={'project':project_list[0]})
        activity_for = forms.ChoiceField(choices=hirarchy_tuple, label='Activity For*')
        milestone = forms.ModelChoiceField(queryset=milestone_list, required=False)
        training = forms.ModelChoiceField(queryset=training_list, required=False)
        strategy = forms.ModelChoiceField(queryset=strategy_list, required=False)

        class Meta:
            model = Activity
            fields = ['title', 'activity_for', 'milestone', 'training', 'strategy',
                      'activity_type', 'description', 'proposed_start_date', 'proposed_end_date',
                      'actual_start_date', 'actual_end_date',
                      'status', 'budget', 'amount_spent', 'challenges', 'achivements', 'remarks']
    return cus_activity_form

class project_reports_form(forms.Form):
    ''' form for filter by project type,status,start date end date '''

    project_type_list = Project_Type.objects.filter(active=2)
    activity_status_list = Activity_Status.objects.filter(active=2)

    project_type = forms.ModelChoiceField(queryset=project_type_list, required=False)
    project_status = forms.ModelChoiceField(queryset=activity_status_list, required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
