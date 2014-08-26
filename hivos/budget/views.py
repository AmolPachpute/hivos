from django.shortcuts import render
from budget.models import Activity_Status, Budget, Budget_Activity, Budget_Strategy
from usermanagement.models import *
from budget.forms import *
from django.shortcuts import render_to_response, RequestContext, HttpResponse
import json

def home(request):
    ''' Budget home '''

    menus = Menus.objects.filter(parent=None, active=2)
    return render(request, 'budget/budget_home.html', locals())

def main_data(request):
    key = request.GET.get('key')
    resource = []

    if key == 'budget-activity-status':
        item_list = Activity_Status.objects.all().order_by('-created_on')
    if key == 'budget':
        item_list = Budget.objects.all().order_by('-created_on')

    return render(request, 'budget/budget_replace.html', locals())


def budget_details(request):
    ''' to list all  activities and strategies related to that budget '''

    budget_id = int(request.GET['budget_id'])  # required in template
    budget_obj = Budget.objects.get(id=budget_id)
    activity_list = Budget_Activity.objects.filter(budget=budget_obj)
    strategy_list = Budget_Strategy.objects.filter(budget=budget_obj)

    return render(request, 'budget/budget_details.html', locals())

def manage_activity_status(request, value=None):

    """ budget activity status record management funtions """
    response = {}
    success = False
    msg = ''

    if value == "add":
        form = Activity_Status_Form()
        if request.method == "POST":
            form = Activity_Status_Form(request.POST)
            if form.is_valid():
                activity_exists = Activity_Status.objects.filter(name__iexact=request.POST.get('name'))
                if activity_exists:
                    msg = "Activity status with this name already exists"
                else:
                    form.save()
                    added = True
                    msg = "Activity status added successfully"
                    success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        activity_status_obj = Activity_Status.objects.get(id=id_edit)
        form = Activity_Status_Form(instance=activity_status_obj)
        if request.method == 'POST':
            form = Activity_Status_Form(request.POST, instance=activity_status_obj)
            if form.is_valid():
                activity_status = Activity_Status.objects.filter(name=request.POST.get('name', "")).exclude(id=int(id_edit))
                if activity_status:
                    msg = "Activity status with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Activity status edited successfully"
                    success = True
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        activity_status = Activity_Status.objects.get(id=id_del)
        activity_status.active = 0
        activity_status.save()
        msg = "Activity status deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        activity_status = Activity_Status.objects.get(id=active)
        activity_status.active = 2
        activity_status.save()
        msg = "Activity status activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('budget/add_edit_activity_status.html', locals(), context_instance=RequestContext(request))

def manage_budget(request, value=None):

    """ budget record management funtions """
    response = {}
    success = False
    msg = ''

    if value == "add":
        form = Budget_Form()
        if request.method == "POST":
            form = Budget_Form(request.POST)
            if form.is_valid():
                budget_exists = Budget.objects.filter(title=request.POST['title'])
                if budget_exists:
                    msg = 'Budget with this title already exists'
                else:
                    form.save()
                    added = True
                    msg = "Budget added successfully"
                    success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        budget_obj = Budget.objects.get(id=id_edit)
        form1 = edit_budget(budget_obj.id)
        form = form1(instance=budget_obj)
        if request.method == 'POST':
            form = form1(request.POST, instance=budget_obj)
            if form.is_valid():
                budget_exists = Budget.objects.filter(title=request.POST['title']).exclude(id=int(id_edit))
                if budget_exists:
                    msg = 'Budget with this title already exists'
                else:
                    form.save()
                    edit_done = True
                    msg = "Budget edited successfully"
                    success = True
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        budget_obj = Budget.objects.get(id=id_del)
        budget_obj.active = 0
        budget_obj.save()
        msg = "Budget deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        budget_obj = Budget.objects.get(id=active)
        budget_obj.active = 2
        budget_obj.save()
        msg = "Budget activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('budget/add_edit_budget.html', locals(), context_instance=RequestContext(request))

def manage_budget_strategy(request, value=None):

    """ budget strategy management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Budget_Strategy_Form()
        budget_id = int(request.GET['budget_id'])
        budget_obj = Budget.objects.get(id=budget_id)
        if request.method == "POST":
            form = Budget_Strategy_Form(request.POST)
            if form.is_valid():
                st_exists = Budget_Strategy.objects.filter(budget=budget_obj, title=request.POST['title']).exists()
                if st_exists:
                    msg = 'Strategy with this title already exists'
                else:
                    form2 = form.save(commit=False)
                    form2.budget = budget_obj
                    form2.save()
                    added = True
                    msg = "Strategy added successfully"
                    success = True
                    strategy_list = Budget_Strategy.objects.filter(budget=budget_obj).order_by('-created_on')
                    return render_to_response('budget/list_strategies.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        budget_id = request.GET.get('budget_id')
        strategy_obj = Budget_Strategy.objects.get(id=id_edit)
        budget_obj = Budget.objects.get(id=budget_id)
        form = Budget_Strategy_Form(instance=strategy_obj)
        if request.method == 'POST':
            form = Budget_Strategy_Form(request.POST, instance=strategy_obj)
            if form.is_valid():
                st_exists = Budget_Strategy.objects.filter(budget=budget_obj, title=request.POST['title']).exclude(id=int(id_edit))
                if st_exists:
                    msg = 'Strategy with this title already exists'
                else:
                    form2 = form.save(commit=False)
                    form2.budget = budget_obj
                    form2.save()
                    edit_done = True
                    msg = "Strategy edited successfully"
                    success = True
                    strategy_list = Budget_Strategy.objects.filter(budget=budget_obj).order_by('-created_on')
                    return render_to_response('budget/list_strategies.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        strategy_obj = Budget_Strategy.objects.get(id=id_del)
        strategy_obj.active = 0
        strategy_obj.save()
        msg = "Strategy deactivated successfully"
        strategy_list = Budget_Strategy.objects.filter(budget=strategy_obj.budget).order_by('-created_on')
        return render_to_response('budget/list_strategies.html', locals(), context_instance=RequestContext(request))

    elif value == "active":
        active = request.GET.get('active')
        strategy_obj = Budget_Strategy.objects.get(id=active)
        strategy_obj.active = 2
        strategy_obj.save()
        msg = "Strategy activated successfully"
        strategy_list = Budget_Strategy.objects.filter(budget=strategy_obj.budget).order_by('-created_on')
        return render_to_response('budget/list_strategies.html', locals(), context_instance=RequestContext(request))

    elif value == "cancel":
        budget_id = int(request.GET['budget_id'])
        budget_obj = Budget.objects.get(id=budget_id)
        strategy_list = Budget_Strategy.objects.filter(budget=budget_obj).order_by('-created_on')
        return render_to_response('budget/list_strategies.html', locals(), context_instance=RequestContext(request))

    return render_to_response('budget/add_edit_strategy.html', locals(), context_instance=RequestContext(request))

def manage_budget_activity(request, value=None):

    """ budget strategy management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        budget_id = int(request.GET['budget_id'])
        budget_obj = Budget.objects.get(id=budget_id)
        form = Budget_Activity_Form()
        if request.method == "POST":
            form = Budget_Activity_Form(request.POST)
            if form.is_valid():
                act_exists = Budget_Activity.objects.filter(budget=budget_obj, title=request.POST['title'])
                if act_exists:
                    msg = "Activity wth this title for this budget already exists"
                else:
                    form2 = form.save(commit=False)
                    form2.budget = budget_obj
                    form2.save()
                    added = True
                    msg = "Activity added successfully"
                    success = True
                    activity_list = Budget_Activity.objects.filter(budget=budget_obj).order_by('-created_on')
                    return render_to_response('budget/list_activities.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        budget_id = request.GET.get('budget_id')
        activity_obj = Budget_Activity.objects.get(id=id_edit)
        budget_obj = Budget.objects.get(id=budget_id)
        form = Budget_Activity_Form(instance=activity_obj)
        if request.method == 'POST':
            form = Budget_Activity_Form(request.POST, instance=activity_obj)
            if form.is_valid():
                act_exists = Budget_Activity.objects.filter(budget=budget_obj, title=request.POST['title']).exclude(id=int(id_edit))
                if act_exists:
                    msg = "Activity wth this title for this budget already exists"
                else:
                    form2 = form.save(commit=False)
                    form2.budget = budget_obj
                    form2.save()
                    edit_done = True
                    msg = "Activity edited successfully"
                    success = True
                    activity_list = Budget_Activity.objects.filter(budget=budget_obj).order_by('-created_on')
                    return render_to_response('budget/list_activities.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        activity_obj = Budget_Activity.objects.get(id=id_del)
        activity_obj.active = 0
        activity_obj.save()
        msg = "Activity deactivated successfully"
        activity_list = Budget_Activity.objects.filter(budget=activity_obj.budget).order_by('-created_on')
        return render_to_response('budget/list_activities.html', locals(), context_instance=RequestContext(request))

    elif value == "active":
        active = request.GET.get('active')
        activity_obj = Budget_Activity.objects.get(id=active)
        activity_obj.active = 2
        activity_obj.save()
        msg = "Activity activated successfully"
        activity_list = Budget_Activity.objects.filter(budget=activity_obj.budget).order_by('-created_on')
        return render_to_response('budget/list_activities.html', locals(), context_instance=RequestContext(request))

    elif value == "cancel":
        budget_id = int(request.GET['budget_id'])
        budget_obj = Budget.objects.get(id=budget_id)
        activity_list = Budget_Activity.objects.filter(budget=budget_obj).order_by('-created_on')
        return render_to_response('budget/list_activities.html', locals(), context_instance=RequestContext(request))

    return render_to_response('budget/add_edit_activity.html', locals(), context_instance=RequestContext(request))
