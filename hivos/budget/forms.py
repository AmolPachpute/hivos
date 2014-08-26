from django import forms
from budget.models import Activity_Status, Budget, Budget_Activity, Budget_Strategy

class Activity_Status_Form(forms.ModelForm):
    class Meta:
        model = Activity_Status
        exclude = ('created_on', 'active')

class Budget_Form(forms.ModelForm):

    budget_list = Budget.objects.filter(parent=None, active=2)
    parent = forms.ModelChoiceField(queryset=budget_list,required=False)
    class Meta:

        model = Budget
        exclude = ('created_on', 'active')

def edit_budget(edit_id):
    class Edit_Budget_Form(forms.ModelForm):

        budget_list = Budget.objects.filter(parent=None, active=2).exclude(id=edit_id)
        parent = forms.ModelChoiceField(queryset=budget_list,required=False)
        class Meta:

            model = Budget
            exclude = ('created_on', 'active')
    return Edit_Budget_Form

class Budget_Strategy_Form(forms.ModelForm):
    class Meta:
        model = Budget_Strategy
        exclude = ('created_on', 'active', 'budget')

class Budget_Activity_Form(forms.ModelForm):
    class Meta:
        model = Budget_Activity
        exclude = ('created_on', 'active', 'budget')
