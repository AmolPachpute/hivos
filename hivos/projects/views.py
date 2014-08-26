from projects.models import *
from usermanagement.models import *
from django.shortcuts import render, render_to_response, RequestContext, HttpResponse, HttpResponseRedirect
from projects.forms import *
import json
from django.forms.fields import DateField
from django.contrib.contenttypes.models import ContentType
def home(request):

    menus = Menus.objects.filter(parent=None, active=2)
    return render(request, 'projects/projects_home.html', locals())

def main_data(request):
    key = request.GET.get('key')
    resource = []
    if key == 'activity-status':
        item_list = Activity_Status.objects.all().order_by('-created_on')
    if key == 'coordinator-type':
        item_list = Coordinator_Type.objects.all().order_by('-created_on')
    if key == 'project-type':
        item_list = Project_Type.objects.all().order_by('-created_on')
    if key == 'activity-type':
        item_list = Activity_Type.objects.all().order_by('-created_on')
    if key == 'project':
        item_list = Project.objects.all().order_by('-created_on')
    if key == 'coordinator':
        item_list = Project_Coordinators.objects.all().order_by('-created_on')
    if key == 'budget-head':
        item_list = Budget_Head.objects.all().order_by('-created_on')
    if key == 'milestone':
        item_list = Milestone.objects.all().order_by('-created_on')
    if key == 'project-training':
        item_list = Training.objects.all().order_by('-created_on')
    if key == 'project-filters':
        form = project_reports_form()
        return render(request, 'projects/project_search.html', locals())

    return render(request, 'projects/master_replace.html', locals())


def manage_project_details(request, value=None):

    """ project details i.e milestones,trainings,strategies and activities related to that project """
    project_id = int(request.GET.get('project_id', ''))
    project_obj = Project.objects.get(id=project_id)
    milestone_list = Milestone.objects.filter(project=project_obj)
    milestone_ids = [i.id for i in milestone_list]
    project_training_list = get_all_trainings(project_id, milestone_ids)
    project_training_ids = [i.id for i in project_training_list]
    strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
    strategy_ids = [i.id for i in strategy_list]
    activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
    return render_to_response('projects/project_info.html', locals(), context_instance=RequestContext(request))

def get_all_trainings(project_id, milestone_ids):
    project_training_list = list(Training.objects.filter(content_type__name__iexact='project', object_id=project_id).order_by('-created_on'))
    project_training_list2 = list(Training.objects.filter(content_type__name__iexact='milestone', object_id__in=milestone_ids).order_by('-created_on'))
    [project_training_list.append(i) for i in project_training_list2] #combine all trainings to display project_training_list in template
    return project_training_list

def get_all_strategies(project_id, milestone_ids, project_training_ids):
    strategy_list = list(Strategy.objects.filter(content_type__model__iexact='project', object_id=project_id).order_by('-created_on'))
    strategy_list2 = list(Strategy.objects.filter(content_type__model__iexact='milestone', object_id__in=milestone_ids).order_by('-created_on'))
    strategy_list3 = list(Strategy.objects.filter(content_type__model__iexact='training', object_id__in=project_training_ids).order_by('-created_on'))
    [strategy_list.append(i) for i in strategy_list2] #combine all strategy to display strategy_list in template
    [strategy_list.append(i) for i in strategy_list3] #combine all strategy to display strategy_list in template
    return strategy_list

def get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids):
    activity_list = list(Activity.objects.filter(content_type__model__iexact='project', object_id=project_id).order_by('-created_on'))
    activity_list2 = list(Activity.objects.filter(content_type__model__iexact='milestone', object_id__in=milestone_ids).order_by('-created_on'))
    activity_list3 = list(Activity.objects.filter(content_type__model__iexact='training', object_id__in=project_training_ids).order_by('-created_on'))
    activity_list4 = list(Activity.objects.filter(content_type__model__iexact='strategy', object_id__in=strategy_ids).order_by('-created_on'))
    [activity_list.append(i) for i in activity_list2] #combine all acitity to display acitvity list in template
    [activity_list.append(i) for i in activity_list3] #combine all acitity to display acitvity list in template
    [activity_list.append(i) for i in activity_list4] #combine all acitity to display acitvity list in template
    return activity_list

def manage_activity_status(request, value=None):

    """ activity record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Activity_Status_Form()
        if request.method == "POST":
            form = Activity_Status_Form(request.POST)
            if form.is_valid():
                activity_status_list = Activity_Status.objects.filter(name__iexact=request.POST.get('name'))
                if activity_status_list:
                    msg = 'Activity status with this name already exists'
                else:
                    form.save()
                    added = True
                    msg = "Activity status added successfully"
                    success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        activity_status_obj = Activity_Status.objects.get(id=id_edit)
        form = Activity_Status_Form(instance=activity_status_obj)
        if request.method == 'POST':
            form = Activity_Status_Form(request.POST, instance=activity_status_obj)
            if form.is_valid():
                activity_status = Activity_Status.objects.filter(name__iexact=request.POST.get('name', "")).exclude(id=int(id_edit))
                if activity_status:
                    msg = "Activity status with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Activity status edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
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

    return render_to_response('projects/add_edit_activity_status.html', locals(), context_instance=RequestContext(request))

def manage_coordinator_type(request, value=None):

    """ Coordinator type record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Coordinator_Type_Form()
        if request.method == "POST":
            form = Coordinator_Type_Form(request.POST)
            if form.is_valid():
                coordinator_type = Coordinator_Type.objects.filter(name__iexact=request.POST.get('name', ""))
                if coordinator_type:
                    msg = "Coordinator type with this name already exists"
                else:
                    form.save()
                    added = True
                    msg = "Coordinator type added successfully"
                    success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        coordinator_type_obj = Coordinator_Type.objects.get(id=id_edit)
        form = Coordinator_Type_Form(instance=coordinator_type_obj)
        if request.method == 'POST':
            form = Coordinator_Type_Form(request.POST, instance=coordinator_type_obj)
            if form.is_valid():
                coordinator_type = Coordinator_Type.objects.filter(name__iexact=request.POST.get('name', "")).exclude(id=int(id_edit))
                if coordinator_type:
                    msg = "Coordinator type with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Coordinator type edited successfully"
                    success = True
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        coordinator_type = Coordinator_Type.objects.get(id=id_del)
        coordinator_type.active = 0
        coordinator_type.save()
        msg = "Coordinator type Deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        coordinator_type = Coordinator_Type.objects.get(id=active)
        coordinator_type.active = 2
        coordinator_type.save()
        msg = "Coordinator type activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('projects/add_edit_coordinator_type.html', locals(), context_instance=RequestContext(request))

def manage_project_type(request, value=None):

    """ Coordinator type record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Project_Type_Form()
        if request.method == "POST":
            form = Project_Type_Form(request.POST)
            if form.is_valid():
                project_type_list = Project_Type.objects.filter(name__iexact=request.POST.get('name'))
                if project_type_list:
                    msg = "Project type with this name alreary exists"
                else:
                    form.save()
                    added = True
                    msg = "Project type added successfully"
                    success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        project_type_obj = Project_Type.objects.get(id=id_edit)
        form = Project_Type_Form(instance=project_type_obj)
        if request.method == 'POST':
            form = Project_Type_Form(request.POST, instance=project_type_obj)
            if form.is_valid():
                project_type = Project_Type.objects.filter(name=request.POST.get('name', "")).exclude(id=int(id_edit))
                if project_type:
                    msg = "Project type with this name alreary exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Project type edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        project_type = Project_Type.objects.get(id=id_del)
        project_type.active = 0
        project_type.save()
        msg = "Project type deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        project_type = Project_Type.objects.get(id=active)
        project_type.active = 2
        project_type.save()
        msg = "Project type activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('projects/add_edit_project_type.html', locals(), context_instance=RequestContext(request))

def manage_activity_type(request, value=None):

    """ activity type record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Activity_Type_Form()
        if request.method == "POST":
            form = Activity_Type_Form(request.POST)
            if form.is_valid():
                activitytype = Activity_Type.objects.filter(name__iexact=request.POST.get('name'))
                if activitytype:
                    msg = "Activity type with this name already exists"
                else:
                    form.save()
                    added = True
                    msg = "Activity type added successfully"
                    success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        activity_type_obj = Activity_Type.objects.get(id=id_edit)
        form = Activity_Type_Form(instance=activity_type_obj)
        if request.method == 'POST':
            form = Activity_Type_Form(request.POST, instance=activity_type_obj)
            if form.is_valid():
                activity_type = Activity_Type.objects.filter(name=request.POST.get('name', "")).exclude(id=int(id_edit))
                if activity_type:
                    msg = "Activity type with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Activity type edited successfully"
                    success = True
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        activity_type = Activity_Type.objects.get(id=id_del)
        activity_type.active = 0
        activity_type.save()
        msg = "Activity type deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        activity_type = Activity_Type.objects.get(id=active)
        activity_type.active = 2
        activity_type.save()
        msg = "Activity type activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('projects/add_edit_activity_type.html', locals(), context_instance=RequestContext(request))

def manage_project(request, value=None):

    """ activity type record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Project_Form()
        if request.method == "POST":
            form = Project_Form(request.POST)
            if form.is_valid():
                d = DateField()
                start_date = d.to_python(request.POST['start_date'])
                end_date = d.to_python(request.POST['end_date'])
                from datetime import timedelta
                project_type_obj = Project_Type.objects.get(id=int(request.POST['project_type']))
                pr_list = []
                proj_list = Project.objects.filter(project_type=project_type_obj.id, name__iexact=request.POST.get('name'))
                flag = 0
                for i in proj_list:
                    delta1 = i.end_date - i.start_date
                    dates_between1 = []
                    delta2 = end_date - start_date
                    dates_between2 = []
                    [dates_between1.append(i.start_date + timedelta(j)) for j in range(delta1.days+1)]
                    [dates_between2.append(start_date + timedelta(j)) for j in range(delta2.days+1)]
                    for i in dates_between2:
                        if i in dates_between1:
                            flag = 1
                            msg = "Project with this name already exists between these dates"
                if flag == 0:
                    activity_status_obj = Activity_Status.objects.get(id=int(request.POST['status']))
                    project_obj = Project.objects.create(project_type=project_type_obj, name=request.POST['name'], projectId=request.POST.get('projectId', None),
                    description=request.POST.get('description', None), objective=request.POST.get('objective', None), \
                    start_date=start_date, end_date=end_date, \
                    budget=request.POST.get('budget', None), status=activity_status_obj)
                    if request.POST.getlist('groups', None):
                        gr_list = [int(i) for i in request.POST.getlist('groups')]
                        for i in gr_list:
                            gr_obj = Group.objects.get(id=i)
                            project_obj.groups.add(gr_obj)
                            project_obj.save()
                    if request.POST.getlist('members', None):
                        gr_list = [int(i) for i in request.POST.getlist('members')]
                        for i in gr_list:
                            gr_obj = Farmer.objects.get(id=i)
                            project_obj.members.add(gr_obj)
                            project_obj.save()
                    added = True
                    msg = "Project added successfully"
                    success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        project_obj = Project.objects.get(id=id_edit)
        form = Project_Form(instance=project_obj)
        if request.method == 'POST':
            form = Project_Form(request.POST, instance=project_obj)
            if form.is_valid():
                d = DateField()
                start_date = d.to_python(request.POST['start_date'])
                end_date = d.to_python(request.POST['end_date'])
                from datetime import timedelta
                project_type_obj = Project_Type.objects.get(id=int(request.POST['project_type']))
                pr_list = []
                proj_list = Project.objects.filter(project_type=project_type_obj.id, name__iexact=request.POST.get('name')).exclude(id=int(id_edit))
                flag = 0
                for i in proj_list:
                    delta1 = i.end_date - i.start_date
                    dates_between1 = []
                    delta2 = end_date - start_date
                    dates_between2 = []
                    [dates_between1.append(i.start_date + timedelta(j)) for j in range(delta1.days+1)]
                    [dates_between2.append(start_date + timedelta(j)) for j in range(delta2.days+1)]
                    for i in dates_between2:
                        if i in dates_between1:
                            flag = 1
                            msg = "Project with this name already exists between these dates"
                if flag == 0:
                    project_obj.project_type = Project_Type.objects.get(id=int(request.POST['project_type']))
                    project_obj.name = request.POST['name']
                    project_obj.projectId = request.POST.get('name', None)
                    project_obj.description = request.POST.get('description', None)
                    project_obj.objective = request.POST.get('objective', None)
                    project_obj.budget = request.POST.get('budget', None)
                    project_obj.status = Activity_Status.objects.get(id=int(request.POST['status']))

                    d = DateField()
                    start_date = None;end_date = None
                    if request.POST.get('start_date', ''):
                        start_date = d.to_python(request.POST['start_date'])
                    if request.POST.get('end_date', ''):
                        end_date = d.to_python(request.POST['end_date'])

                    project_obj.start_date = start_date
                    project_obj.end_date = end_date

                    project_obj.save()

                    edit_done = True
                    msg = "Project edited successfully"
                    success = True
            else:
                if form.non_field_errors():
                    msg = [i for i in form.non_field_errors()]
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        project = Project.objects.get(id=id_del)
        project.active = 0
        project.save()
        msg = "Project deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        project = Project.objects.get(id=active)
        project.active = 2
        project.save()
        msg = "Project activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('projects/add_edit_project.html', locals(), context_instance=RequestContext(request))

def manage_project_coordinator(request, value=None):

    """ Coordinator type record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Project_Coordinator_Form()
        if request.method == "POST":
            form = Project_Coordinator_Form(request.POST)
            if form.is_valid():
                cood_exists = Project_Coordinators.objects.filter(project=int(request.POST['project']), staff=int(request.POST['staff']), coordinator_type=int(request.POST['coordinator_type']))
                if cood_exists:
                    msg = "Staff already exists for this project and type"
                else:
                    form.save()
                    added = True
                    msg = "Coordinator added successfully"
                    success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        coordinator_type_obj = Project_Coordinators.objects.get(id=id_edit)
        form = Project_Coordinator_Form(instance=coordinator_type_obj)
        if request.method == 'POST':
            form = Project_Coordinator_Form(request.POST, instance=coordinator_type_obj)
            if form.is_valid():
                cood_exists = Project_Coordinators.objects.filter(project=int(request.POST['project']), staff=int(request.POST['staff']), coordinator_type=int(request.POST['coordinator_type'])).exclude(id=int(id_edit))
                if cood_exists:
                    msg = "Staff already exists for this project and type"
                else:
                    form.save()
                    edit_done = True
                    msg = "Coordinator edited successfully"
                    success = True
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        coordinator = Project_Coordinators.objects.get(id=id_del)
        coordinator.active = 0
        coordinator.save()
        msg = "Coordinator deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        coordinator = Project_Coordinators.objects.get(id=active)
        coordinator.active = 2
        coordinator.save()
        msg = "Coordinator activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('projects/add_edit_project_coordinator.html', locals(), context_instance=RequestContext(request))

def manage_budget_head(request, value=None):

    """ Coordinator type record management funtions """
    response = {}
    success = False
    msg = ''
    if value == "add":
        form = Budget_Head_Form()
        if request.method == "POST":
            form = Budget_Head_Form(request.POST)
            if form.is_valid():
                budget_head_exists = Budget_Head.objects.filter(project__id=int(request.POST.get('project')), name__iexact=request.POST['name'])
                if budget_head_exists:
                    msg = "Budget head for this project already exists"
                else:
                    form.save()
                    added = True
                    msg = "Budget head added successfully"
                    success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        budget_head_obj = Budget_Head.objects.get(id=id_edit)
        form = Budget_Head_Form(instance=budget_head_obj)
        if request.method == 'POST':
            form = Budget_Head_Form(request.POST, instance=budget_head_obj)
            if form.is_valid():
                budget_head_exists = Budget_Head.objects.filter(project__id=int(request.POST.get('project')), name__iexact=request.POST['name']).exclude(id=int(id_edit))
                if budget_head_exists:
                    msg = "Budget head for this project already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Budget head edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        budget_head_obj = Budget_Head.objects.get(id=id_del)
        budget_head_obj.active = 0
        budget_head_obj.save()
        msg = "Budget head deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "active":
        active = request.GET.get('active')
        budget_head_obj = Budget_Head.objects.get(id=active)
        budget_head_obj.active = 2
        budget_head_obj.save()
        msg = "Budget head activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype="application/json")

    return render_to_response('projects/add_edit_budget_head.html', locals(), context_instance=RequestContext(request))

def manage_milestone(request, value=None):

    """ Milestone record management funtions """
    response = {}
    success = False
    msg = ''
    project_id = request.GET.get('project_id','')
    if project_id:
        project_obj = Project.objects.get(id=int(project_id))
    if value == "add":
        form = Milestone_Form()
        if request.method == "POST":

            form = Milestone_Form(request.POST)
            if form.is_valid():
                milestone_title_exists = Milestone.objects.filter(project=project_obj, title__iexact=request.POST.get("title")).exists()
                if milestone_title_exists:
                    msg = "Milestone with this title already exists"
                else:
                    form2 = form.save(commit=False)
                    form2.project = project_obj
                    form2.save()
                    added = True
                    msg = "Milestone added successfully"
                    success = True
                    milestone_list = Milestone.objects.filter(project=project_obj).order_by('-created_on')
                    return render_to_response('projects/list_milestones.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        milestone_obj = Milestone.objects.get(id=id_edit)
        form = Milestone_Form(instance=milestone_obj)
        if request.method == 'POST':
            form = Milestone_Form(request.POST, instance=milestone_obj)
            if form.is_valid():
                milestone_title_exists = Milestone.objects.filter(project=project_obj, title__iexact=request.POST.get("title")).exclude(id=int(id_edit))
                if milestone_title_exists:
                    msg = "Milestone with this title already exists"
                else:
                    form2 = form.save(commit=False)
                    form2.project = project_obj
                    form2.save()
                    edit_done = True
                    msg = "Milestone edited successfully"
                    success = True
                    milestone_list = Milestone.objects.filter(project=project_obj).order_by('-created_on')
                    return render_to_response('projects/list_milestones.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "delete":
        id_del = request.GET.get('id_del')
        milestone_obj = Milestone.objects.get(id=id_del)
        milestone_obj.active = 0
        milestone_obj.save()
        msg = "Milestone  deactivated successfully"
        milestone_list = Milestone.objects.filter(project=milestone_obj.project).order_by('-created_on')
        return render_to_response('projects/list_milestones.html', locals(), context_instance=RequestContext(request))

    elif value == "active":
        active = request.GET.get('active')
        milestone_obj = Milestone.objects.get(id=active)
        milestone_obj.active = 2
        milestone_obj.save()
        msg = "Milestone activated successfully"
        milestone_list = Milestone.objects.filter(project=milestone_obj.project).order_by('-created_on')
        return render_to_response('projects/list_milestones.html', locals(), context_instance=RequestContext(request))

    elif value == "cancel":
        milestone_list = Milestone.objects.filter(project=project_obj).order_by('-created_on')
        return render_to_response('projects/list_milestones.html', locals(), context_instance=RequestContext(request))

    return render_to_response('projects/add_edit_milestone.html', locals(), context_instance=RequestContext(request))

from django.forms.fields import DateField
def manage_project_training(request, value=None):

    """Project Training management funtions """
    response = {}
    success = False
    msg = ''
    project_id = request.GET.get('project_id','')
    if project_id:
        project_obj = Project.objects.get(id=int(project_id))
    milestone_list = Milestone.objects.filter(project=project_obj)
    milestone_ids = [i.id for i in milestone_list] # for displaying all trainings for this milestones
    if value == "add":
        form = Project_Training_Form(int(project_id))
        if request.method == "POST":
            form = form(request.POST)
            if form.is_valid():
                project_training_list = get_all_trainings(project_id, milestone_ids)
                training_title_exists = False
                for i in project_training_list:
                    if request.POST.get('training_title').lower() == i.program.title.lower():
                        training_title_exists = True
                        break
                if training_title_exists:
                    msg = "Training with this title already exists"
                else:
                    d = DateField()
                    start_date = d.to_python(request.POST.get('start_date'))
                    end_date = d.to_python(request.POST['end_date'])
                    program_obj = Program.objects.create(title=request.POST.get('training_title'), description=request.POST.get('description', ''), \
                                           venue=request.POST.get('venue'), start_date=start_date, end_date=end_date, \
                                           batch_size=request.POST.get('batch_size', ''), language=request.POST.get('language'), \
                                            program_objective=request.POST.get('program_objective', ''), \
                                           program_fees=request.POST.get('program_fees', ''))
                    content_type = ContentType.objects.get(name__iexact='project')
                    object_id = project_obj.id
                    if request.POST.get('milestone', ''):
                        content_type = ContentType.objects.get(name__iexact='milestone')
                        object_id = int(request.POST.get('milestone'))
                    Training.objects.create(content_type=content_type, object_id=object_id, program=program_obj)
                    added = True
                    msg = "Training added successfully"
                    success = True
                    project_training_list = get_all_trainings(project_id, milestone_ids)
                    return render_to_response('projects/list_trainings.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = int(request.GET.get('id_edit'))
        project_training_obj = Training.objects.get(id=id_edit)
        if request.method == 'POST':

            form = Project_Training_Form(project_obj.id)
            form = form(request.POST, request.FILES)
            if form.is_valid():
                project_training_list = get_all_trainings(project_id, milestone_ids)
                training_title_exists = False
                for i in project_training_list:
                    if request.POST.get('training_title').lower() == i.program.title.lower() and i.id != int(id_edit):
                        training_title_exists = True
                        break
                if training_title_exists:
                    msg = "Training with this title already exists"
                else:
                    content_type = ContentType.objects.get(name__iexact='project')
                    object_id = project_obj.id
                    if request.POST.get('training_for','') == 'milestone':
                        content_type = ContentType.objects.get(model__iexact='milestone')
                        object_id = int(request.POST['milestone'])
                    program_obj = project_training_obj.program
                    program_obj.title = request.POST.get('training_title')
                    program_obj.description = request.POST.get('description', '')
                    program_obj.venue = request.POST.get('venue')
                    d = DateField()
                    program_obj.start_date = d.to_python(request.POST.get('start_date'))
                    program_obj.end_date = d.to_python(request.POST.get('end_date'))
                    program_obj.batch_size = request.POST.get('batch_size', '')
                    program_obj.language = request.POST.get('language')
                    program_obj.program_objective = request.POST.get('program_objective', '')
                    program_obj.program_fees = request.POST.get('program_fees', '')
                    program_obj.save()
                    project_training_obj.content_type = content_type
                    project_training_obj.object_id = object_id
                    project_training_obj.program = program_obj
                    project_training_obj.save()
                    edit_done = True
                    msg = "Training edited successfully"
                    success = True
                    project_training_list = get_all_trainings(project_id, milestone_ids)
                    return render_to_response('projects/list_trainings.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")
        else:

            milestone_obj = None
            if project_training_obj.content_type.name == "project":
                project_obj = Project.objects.get(id=project_training_obj.object_id)
                form = Project_Training_Form(project_obj.id)
            if project_training_obj.content_type.name == "milestone":
                milestone_obj = Milestone.objects.get(id=project_training_obj.object_id)
                project_obj = milestone_obj.project
                form = Project_Training_Form(project_obj.id)
            form = form(initial={'project':project_obj, 'training_for':project_training_obj.content_type.name,
            'milestone':milestone_obj,
            'training_title':project_training_obj.program.title, 'description':project_training_obj.program.description,
            'venue':project_training_obj.program.venue,
            'start_date':project_training_obj.program.start_date, 'end_date':project_training_obj.program.end_date,
            'batch_size':project_training_obj.program.batch_size,
            'language':project_training_obj.program.language, 'program_objective':project_training_obj.program.program_objective,
            'program_fees':project_training_obj.program.program_fees})

    elif value == "delete":
        id_del = request.GET.get('id_del')
        project_training_obj = Training.objects.get(id=id_del)
        project_training_obj.active = 0
        project_training_obj.save()
        msg = "Training  deactivated successfully"
        project_training_list = get_all_trainings(project_id, milestone_ids)
        return render_to_response('projects/list_trainings.html', locals(), context_instance=RequestContext(request))

    elif value == "active":
        active = request.GET.get('active')
        project_training_obj = Training.objects.get(id=active)
        project_training_obj.active = 2
        project_training_obj.save()
        msg = "Training activated successfully"
        project_training_list = get_all_trainings(project_id, milestone_ids)
        return render_to_response('projects/list_trainings.html', locals(), context_instance=RequestContext(request))

    elif value == "cancel":
        project_training_list = get_all_trainings(project_id, milestone_ids)
        return render_to_response('projects/list_trainings.html', locals(), context_instance=RequestContext(request))

    return render_to_response('projects/add_edit_project_training.html', locals(), context_instance=RequestContext(request))

def manage_strategy(request, value=None):

    """ Milestone record management funtions """
    response = {}
    success = False
    msg = ''
    project_id = request.GET.get('project_id','')
    if project_id:
        project_obj = Project.objects.get(id=int(project_id))
        milestone_list = Milestone.objects.filter(project=project_obj)
        milestone_ids = [i.id for i in milestone_list]
        project_training_list = get_all_trainings(project_id, milestone_ids)
        project_training_ids = [i.id for i in project_training_list]
    if value == "add":
        form = Stretegy_Form(int(project_id))
        if request.method == "POST":
            form = form(request.POST)
            if form.is_valid():
                strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
                strategy_title_exists = False
                for i in strategy_list:
                    if request.POST.get('title').lower() == i.title.lower():
                        strategy_title_exists = True
                        break
                if strategy_title_exists:
                    msg = "Strategy with this title already exists"
                else:
                    strategy_for = request.POST.get('strategy_for')
                    content_type = ContentType.objects.get(model__iexact='project')
                    object_id = project_id
                    if strategy_for == 'milestone':
                        content_type = ContentType.objects.get(model__iexact='milestone')
                        object_id = int(request.POST.get('milestone'))
                    if strategy_for == 'training':
                        content_type = ContentType.objects.get(model__iexact='training')
                        object_id = int(request.POST.get('training'))
                    form2 = form.save(commit=False)
                    form2.content_type = content_type
                    form2.object_id = object_id
                    form2.save()
                    added = True
                    msg = "Strategy added successfully"
                    success = True
                    strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
                    return render_to_response('projects/list_strategies.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")


    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        strategy_obj = Strategy.objects.get(id=id_edit)
        form = Stretegy_Form(project_id)
        if request.method == 'POST':
            form = form(request.POST, instance=strategy_obj)
            if form.is_valid():
                strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
                strategy_title_exists = False
                for i in strategy_list:
                    if request.POST.get('title').lower() == i.title.lower() and i.id != int(id_edit):
                        strategy_title_exists = True
                        break
                if strategy_title_exists:
                    msg = "Strategy with this title already exists"
                else:
                    strategy_for = request.POST.get('strategy_for')
                    content_type = ContentType.objects.get(model__iexact='project')
                    object_id = project_id
                    if strategy_for == 'milestone':
                        content_type = ContentType.objects.get(model__iexact='milestone')
                        object_id = int(request.POST.get('milestone'))
                    if strategy_for == 'training':
                        content_type = ContentType.objects.get(model__iexact='training')
                        object_id = int(request.POST.get('training'))
                    form2 = form.save(commit=False)
                    form2.content_type = content_type
                    form2.object_id = object_id
                    form2.save()
                    edit_done = True
                    msg = "Strategy edited successfully"
                    success = True
                    strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
                    return render_to_response('projects/list_strategies.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")
        else:
            milestone_obj = None;training_obj = None
            if strategy_obj.content_type.model == 'milestone':
                milestone_obj = Milestone.objects.get(id=strategy_obj.object_id)
            if strategy_obj.content_type.model == 'training':
                training_obj = Training.objects.get(id=strategy_obj.object_id)
            form = form(initial={'project':project_obj, 'strategy_for':strategy_obj.content_type.model,
                                 'milestone':milestone_obj, 'training':training_obj,
                                 'title':strategy_obj.title, 'description':strategy_obj.description})

    elif value == "delete":
        id_del = request.GET.get('id_del')
        obj = Strategy.objects.get(id=id_del)
        obj.active = 0
        obj.save()
        msg = "Strategy deactivated successfully"
        strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
        return render_to_response('projects/list_strategies.html', locals(), context_instance=RequestContext(request))

    elif value == "active":
        active = request.GET.get('active')
        obj = Strategy.objects.get(id=active)
        obj.active = 2
        obj.save()
        msg = "Strategy activated successfully"
        strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
        return render_to_response('projects/list_strategies.html', locals(), context_instance=RequestContext(request))

    elif value == "cancel":
        strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
        return render_to_response('projects/list_strategies.html', locals(), context_instance=RequestContext(request))

    return render_to_response('projects/add_edit_strategy.html', locals(), context_instance=RequestContext(request))

def manage_activity(request, value=None):

    """ Activity record management funtions """
    response = {}
    success = False
    msg = ''
    project_id = request.GET.get('project_id','')
    if project_id:
        project_obj = Project.objects.get(id=int(project_id))
        milestone_list = Milestone.objects.filter(project=project_obj)
        milestone_ids = [i.id for i in milestone_list]
        project_training_list = get_all_trainings(project_id, milestone_ids)
        project_training_ids = [i.id for i in project_training_list]
        strategy_list = get_all_strategies(project_id, milestone_ids, project_training_ids)
        strategy_ids = [i.id for i in strategy_list]
    if value == "add":
        form = Activity_Form(int(project_id))
        if request.method == "POST":
            form = form(request.POST)
            if form.is_valid():
                activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
                activity_title_exists = False
                for i in activity_list:
                    if request.POST.get('title').lower() == i.title.lower():
                        activity_title_exists = True
                        break
                if activity_title_exists:
                    msg = "Activity with this title already exists"
                else:
                    activity_for = request.POST.get('activity_for')
                    content_type = ContentType.objects.get(model__iexact='project')
                    object_id = project_id
                    if activity_for == 'milestone':
                        content_type = ContentType.objects.get(model__iexact='milestone')
                        object_id = int(request.POST.get('milestone'))
                    if activity_for == 'training':
                        content_type = ContentType.objects.get(model__iexact='training')
                        object_id = int(request.POST.get('training'))
                    if activity_for == 'strategy':
                        content_type = ContentType.objects.get(model__iexact='strategy')
                        object_id = int(request.POST.get('strategy'))

                    form2 = form.save(commit=False)
                    form2.content_type = content_type
                    form2.object_id = object_id
                    form2.save()

                    added = True
                    msg = "Activity added successfully"
                    success = True
                    activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
                    return render_to_response('projects/list_activities.html', locals(), context_instance=RequestContext(request))
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")

    elif value == "edit":
        id_edit = request.GET.get('id_edit')
        activity_obj = Activity.objects.get(id=int(id_edit))
        form = Activity_Form(project_id)
        if request.method == 'POST':
            form = form(request.POST, instance=activity_obj)
            if form.is_valid():
                activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
                activity_title_exists = False
                for i in activity_list:
                    if request.POST.get('title').lower() == i.title.lower() and i.id != int(id_edit):
                        activity_title_exists = True
                        break
                if activity_title_exists:
                    msg = "Activity with this title already exists"
                else:
                    activity_for = request.POST.get('activity_for')
                    content_type = ContentType.objects.get(model__iexact='project')
                    object_id = project_id
                    if activity_for == 'milestone':
                        content_type = ContentType.objects.get(model__iexact='milestone')
                        object_id = int(request.POST.get('milestone'))
                    if activity_for == 'training':
                        content_type = ContentType.objects.get(model__iexact='training')
                        object_id = int(request.POST.get('training'))
                    if activity_for == 'strategy':
                        content_type = ContentType.objects.get(model__iexact='strategy')
                        object_id = int(request.POST.get('strategy'))
                    form2 = form.save(commit=False)
                    form2.content_type = content_type
                    form2.object_id = object_id
                    form2.save()

                    edit_done = True
                    msg = "Activity edited successfully"
                    success = True
                    activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
                    return render_to_response('projects/list_activities.html', locals(), context_instance=RequestContext(request))
            else:

                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype="application/json")
        else:
            milestone_obj = None;training_obj = None;strategy_obj = None
            if activity_obj.content_type.model == 'milestone':
                milestone_obj = Milestone.objects.get(id=activity_obj.object_id)
            if activity_obj.content_type.model == 'training':
                training_obj = Training.objects.get(id=activity_obj.object_id)
            if activity_obj.content_type.model == 'strategy':
                strategy_obj = Strategy.objects.get(id=activity_obj.object_id)
            form = form(initial={'project':project_obj, 'activity_for':activity_obj.content_type.model,
                                 'milestone':milestone_obj, 'training':training_obj, 'strategy':strategy_obj,
                                 'title':activity_obj.title, 'description':activity_obj.description}, instance=activity_obj)

    elif value == "delete":
        id_del = request.GET.get('id_del')
        obj = Activity.objects.get(id=id_del)
        obj.active = 0
        obj.save()
        msg = "Strategy deactivated successfully"
        activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
        return render_to_response('projects/list_activities.html', locals(), context_instance=RequestContext(request))

    elif value == "active":
        active = request.GET.get('active')
        obj = Activity.objects.get(id=active)
        obj.active = 2
        obj.save()
        msg = "Strategy activated successfully"
        activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
        return render_to_response('projects/list_activities.html', locals(), context_instance=RequestContext(request))

    elif value == "cancel":
        activity_list = get_all_activities(project_id, milestone_ids, project_training_ids, strategy_ids)
        return render_to_response('projects/list_activities.html', locals(), context_instance=RequestContext(request))

    return render_to_response('projects/add_edit_activity.html', locals(), context_instance=RequestContext(request))

def get_training(request):
    ''' for ajax requests for drop dropdown '''

    results = {}
    project_id = int(request.GET.get("project_id", ""))
    project_training_list = list(Training.objects.filter(content_type__model__iexact='project', object_id=project_id, active=2).values('id', 'program__title'))
    milestone_list = Milestone.objects.filter(project__id=project_id, active=2)
    milestone_id_list = [i.id for i in milestone_list]
    project_training_list2 = list(Training.objects.filter(content_type__model__iexact='milestone',
        object_id__in=milestone_id_list, active=2).values('id', 'program__title'))
    [project_training_list.append(i) for i in project_training_list2]
    results['res'] = project_training_list

    return HttpResponse(json.dumps(results), mimetype="application/json")

def get_strategy(request):
    ''' for ajax requests for drop dropdown '''

    results = {}
    project_id = int(request.GET.get("project_id", ""))
    project_training_list = Training.objects.filter(content_type__model__iexact='project', object_id=project_id, active=2)
    milestone_list = Milestone.objects.filter(project__id=project_id, active=2)
    milestone_id_list = [i.id for i in milestone_list]
    project_training_list2 = Training.objects.filter(content_type__model__iexact='milestone',
        object_id__in=milestone_id_list, active=2)
    project_training_ids = [i.id for i in project_training_list]
    [project_training_ids.append(i.id) for i in  project_training_list2]
    strategy_list = list(Strategy.objects.filter(content_type__model__iexact='project', object_id=project_id, active=2).values('id', 'title'))
    strategy_list2 = list(Strategy.objects.filter(content_type__model__iexact='milestone', object_id__in=milestone_id_list, active=2).values('id', 'title'))
    strategy_list3 = list(Strategy.objects.filter(content_type__model__iexact='training', object_id__in=project_training_ids, active=2).values('id', 'title'))
    [strategy_list.append(i) for i in strategy_list2]
    [strategy_list.append(i) for i in strategy_list3]
    results['res'] = strategy_list

    return HttpResponse(json.dumps(results), mimetype="application/json")

def project_filters(request):

    project_type = request.POST.get('project_type', None)
    project_status = request.POST.get('project_status', None)
    start_date = request.POST.get('start_date', None)
    #end_date = request.POST.get('end_date', None)
    #import ipdb;ipdb.set_trace()
    #projects_list = Project.objects.filter(project_type=int(project_type)).filter(status=project_status).filter(start_date=start_date).filter(end_date=end_date)
    #key = "project"
    #reason = "filters"

    return render(request, "projects/project_search.html", locals())
