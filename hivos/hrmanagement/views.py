# Create your views here.
from django.shortcuts import render, render_to_response
#from django.http import HttpResponseRedirect
from hrmanagement.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.template import Context, loader, RequestContext
from hrmanagement.forms import *

from django.http import HttpResponseRedirect, HttpResponse
from farmer.models import *
from django.contrib.auth.models import User
from django.forms.fields import DateField
from usermanagement.models import *

def home(request):

    menus = Menus.objects.filter(parent=None, active = 2)
    return render(request, 'hrmanagement/hr_home.html', locals())

def main_data(request):
    key = request.GET.get('key')
    resource = []

    if key == 'staffs':
        item_list = Staff.objects.all().order_by('-created_on')
        title = 'Staff'
    if key == 'department':
       item_list = Department.objects.all().order_by('-created_on')
       title = 'Department'
    if key == 'designation':
       item_list = Designation.objects.all().order_by('-created_on')
       title = 'Designation'
    if key == 'skills-type':
       item_list = Skill_Type.objects.all().order_by('-created_on')
       title = 'Skill Type'
    if key == 'salary':
       item_list = Salary.objects.all().order_by('-created_on')
       title = 'Salary'
    if key == 'skills':
       item_list = Skills.objects.all().order_by('-created_on')
       title = 'Skills'
    if key == 'staff-type':
       item_list = Staff_Type.objects.all().order_by('-created_on')
       title = 'Staff Type'


    return render(request, 'hrmanagement/master_replace.html', locals())



def manage_department(request, task=None):

    """ Department record management funtions """
    response = {}
    success = False
    msg = ''
    if task == "add":
        form = add_department_form()
        if request.method == "POST":
            form = add_department_form(request.POST)
            if form.is_valid():
                dept_obj_list = Department.objects.filter(name__iexact=request.POST.get('name',""))
                if dept_obj_list:
                    if dept_obj_list[0].active == 2:
                        msg = "Department with this name already exists"
                    else:
                        dept_obj_list[0].active = 2
                        dept_obj_list[0].save()
                        added = True
                        msg = "Department added successfully"
                        success = True
                else:
                    form.save()
                    added = True
                    msg = "Department added successfully"
                    success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        department = Department.objects.get(id=id_edit)
        form = add_department_form(instance=department)
        if request.method == 'POST':
            form = add_department_form(request.POST, instance=department)
            if form.is_valid():
                dept_obj_list = Department.objects.filter(name__iexact=request.POST.get('name',"")).exclude(id=int(id_edit))
                if dept_obj_list:
                    msg = "Department with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Department edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="delete":
        id_del = request.GET.get('id_del')
        department = Department.objects.get(id = id_del)
        department.active = 0
        department.save()
        msg = "Department deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        department = Department.objects.get(id = active)
        department.active = 2
        department.save()
        msg = "Department activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_department.html', locals(), context_instance = RequestContext(request))

def manage_staff(request, task=None):

    """ Staff record management funtions """
    response = {}
    success = False
    msg = ''

    if task == "add":
        form = add_staff_form()
        if request.method == "POST":
            form = add_staff_form(request.POST)
            from farmer.models import Position_Type
            if form.is_valid():
                from farmer.models import Maritial_Status
                maritial_status_obj = Maritial_Status.objects.get(id=int(request.POST.get('maritial_status')))

                user_obj = None
                from farmer.models import Salutations
                prefix_obj = Salutations.objects.get(id=int(request.POST.get('prefix')))

                birth_date = ""; leaving_date = ""

                d = DateField()
                joining_date = None;leaving_date = None;birth_date = None
                if request.POST.get('date_of_joining'):
                    joining_date = d.to_python(request.POST.get('date_of_joining',''))
                if request.POST.get('date_of_leaving'):
                    leaving_date = d.to_python(request.POST.get('date_of_leaving',''))
                if request.POST.get('dob'):
                    birth_date = d.to_python(request.POST.get('dob',''))

                from uuid import uuid4
                uuid = uuid4().hex    # generates unique ID

                person_obj = Person.objects.create(first_name=request.POST.get('first_name'),middle_name=request.POST.get('middle_name'),Last_name=request.POST.get('Last_name'),\
                prefix=prefix_obj, farmer_id=request.POST.get('farmer_id'),gender=request.POST.get('gender'),\
                dob= birth_date, maritial_status=maritial_status_obj, uuid=uuid, added_by=request.user)
                from django.template.defaultfilters import slugify

                slug = slugify(str(person_obj.id)+str(person_obj.first_name))
                person_obj.slug = slug
                person_obj.save()

                staff_type_obj = Staff_Type.objects.get(id=int(request.POST.get('staff_type')))
                department_obj = None;designation_obj = None
                if request.POST.get('department'):
                    department_obj = Department.objects.get(id=int(request.POST.get('department')))
                if request.POST.get('designation'):
                    designation_obj = Designation.objects.get(id=int(request.POST.get('designation')))

                staff_obj = Staff.objects.create(staff_type = staff_type_obj, personal_info = person_obj, \
                           department = department_obj, designation=designation_obj, \
                            date_of_joining = joining_date, date_of_leaving = leaving_date, \
                            photo = request.POST.get('photo',''),work_experience = request.POST.get('work_experience','') )

                if request.POST.getlist('skills'):
                    sk_list = [int(i) for i in request.POST.getlist('skills')]
                    for i in sk_list:
                        sk_obj = Skills.objects.get(id= i)
                        staff_obj.skills.add(sk_obj)
                        staff_obj.save()

                from farmer.models import Educational_Qualification
                if request.POST.getlist('qualification'):
                    sk_list = [int(i) for i in request.POST.getlist('qualification')]
                    for i in sk_list:
                        sk_obj = Educational_Qualification.objects.get(id= i)
                        staff_obj.qualification.add(sk_obj)
                        staff_obj.save()
                request.session['staff_id'] = staff_obj.id
                form = add_staff_address_form(staff_obj.id)

                added = True
                msg = "Staff added successfully"
                success = True
                #return  HttpResponseRedirect('/hr/Staff-Address/add/')
                #return render(request, 'hrmanagement/add_edit_staff_address.html', locals())
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        staff_obj = Staff.objects.get(id=int(id_edit))
        person_obj = Person.objects.get(id = staff_obj.personal_info.id)
        form = add_staff_form(initial = {'prefix':person_obj.prefix, 'first_name':person_obj.first_name, \
        'middle_name':person_obj.middle_name, 'Last_name':person_obj.Last_name, \
        'farmer_id':person_obj.farmer_id, \
        'gender':person_obj.gender, 'dob':person_obj.dob, 'maritial_status':person_obj.maritial_status, 'designation':staff_obj.designation, \
        'staff_type':staff_obj.staff_type, 'personal_info':staff_obj.personal_info, 'skills':staff_obj.skills.all(), 'department':staff_obj.department, \
        'qualification':staff_obj.qualification.all(), 'date_of_joining':staff_obj.date_of_joining, 'date_of_leaving':staff_obj.date_of_leaving, \
        'photo':staff_obj.photo, 'work_experience':staff_obj.work_experience})

        if request.method == 'POST':
            form = add_staff_form(request.POST, request.FILES)
            if form.is_valid():
                from farmer.models import Position_Type, Maritial_Status, Educational_Qualification, Salutations
                maritial_status_obj = Maritial_Status.objects.get(id=int(request.POST.get('maritial_status')))

                prefix_obj = Salutations.objects.get(id=int(request.POST.get('prefix')))

                d = DateField()

                person_obj.prefix = prefix_obj;person_obj.first_name = request.POST.get('first_name','')
                person_obj.middle_name = request.POST.get('middle_name','');person_obj.Last_name = request.POST.get('Last_name','')
                person_obj.farmer_id = request.POST.get('farmer_id','')
                person_obj.gender = request.POST.get('gender','')

                if request.POST.get('dob'):
                    birth_date = d.to_python(request.POST.get('dob',''))
                    person_obj.dob = birth_date
                person_obj.maritial_status = maritial_status_obj;person_obj.uuid = request.POST.get('uuid','')

                if request.POST.get('added_by'):
                    user_obj = User.objects.get(id=int(request.POST.get('added_by')))
                    person_obj.added_by = user_obj

                person_obj.save()

                staff_type_obj = Staff_Type.objects.get(id=int(request.POST.get('staff_type')))

                department_obj = None;designation_obj = None
                if request.POST.get('department'):
                    department_obj = Department.objects.get(id=int(request.POST.get('department')))
                if request.POST.get('designation'):
                    designation_obj = Designation.objects.get(id=int(request.POST.get('designation')))

                staff_obj.staff_type = staff_type_obj;staff_obj.personal_info = person_obj
                staff_obj.department = department_obj
                staff_obj.designation = designation_obj
                if request.POST.get('date_of_joining'):
                    joining_date = d.to_python(request.POST.get('date_of_joining',''))
                    staff_obj.date_of_joining = joining_date
                if request.POST.get('date_of_leaving'):
                    leaving_date = d.to_python(request.POST.get('date_of_leaving',''))
                    staff_obj.date_of_leaving = leaving_date
                staff_obj.photo = request.POST.get('photo','')
                staff_obj.work_experience = request.POST.get('work_experience','')
                staff_obj.save()

                if request.POST.getlist('skills'):
                    sk_list = [int(i) for i in request.POST.getlist('skills')]
                    for i in sk_list:
                        sk_obj = Skills.objects.get(id= i)
                        staff_obj.skills.add(sk_obj)
                        staff_obj.save()

                if request.POST.getlist('qualification'):
                    sk_list = [int(i) for i in request.POST.getlist('qualification')]
                    for i in sk_list:
                        sk_obj = Educational_Qualification.objects.get(id= i)
                        staff_obj.qualification.add(sk_obj)
                        staff_obj.save()
                edit_done = True
                msg = "Staff edited successfully"
                success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="delete":
        id_del = request.GET.get('id_del')
        staff = Staff.objects.get(id = id_del)
        staff.active = 0
        staff.save()
        msg = "Staff deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        staff = Staff.objects.get(id = active)
        staff.active = 2
        staff.save()
        msg = "Staff activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_staff.html', locals(), context_instance = RequestContext(request))

def manage_staff_address(request, task=None):

    """ Staff address record management funtions """
    response = {}
    success = False
    msg = ''
    url = ''
    if task == "add":
        staff_obj = Staff.objects.get(id=int(request.session['staff_id']))
        form = add_staff_address_form(staff_obj.id)
        if request.method == "POST":
            form2 = add_staff_address_form(staff_obj.id)
            form = form2(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.staff = staff_obj
                form.save()
                added = True
                msg = "Staff address added successfully"
                success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":

        id_edit = request.GET.get('id_edit')
        from hrmanagement.models import Staff_Address
        staff_obj = Staff.objects.get(id=int(id_edit))
        try:
            staff_address_obj = Staff_Address.objects.get(staff = staff_obj)
        except ObjectDoesNotExist:
            msg = 'Staff address does not exist'
            task = 'no_address'
            key = 'staff-address'
            title = 'Address'
            return render_to_response('hrmanagement/add_edit_staff_address.html', locals(), context_instance = RequestContext(request))
        finally:
            request.session['staff_id'] = staff_obj.id   # for adding staff address store in session for which staff address is to be added

        form = add_staff_address_form(staff_obj.id)
        form = form(instance=staff_address_obj)
        if request.method == 'POST':
            form1 = add_staff_address_form(staff_obj.id)
            form = form1(request.POST, instance=staff_address_obj)
            if form.is_valid():
                form2 = form.save(commit=False)
                form2.staff = staff_obj
                form2.save()
                edit_done = True
                msg = "Staff address edited successfully"
                success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")


    elif task =="delete":
        id_del = request.GET.get('id_del')
        salutation = Salutations.objects.get(id = id_del)
        salutation.active = 0
        salutation.save()
        msg = "Salutation deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        salutation = Salutations.objects.get(id = active)
        salutation.active = 2
        salutation.save()
        msg = "Salutation activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_staff_address.html', locals(), context_instance = RequestContext(request))


def manage_designation(request, task=None):

    """ Designation record management funtions """
    response = {}
    success = False
    msg = ''

    if task == "add":
        form = add_designation_form()
        if request.method == "POST":
            form = add_designation_form(request.POST)
            if form.is_valid():
                desig_obj_list = Designation.objects.filter(name__iexact = request.POST.get('name', ""))
                if desig_obj_list:
                    if desig_obj_list[0].active == 2:
                        msg = "Designation with this name already exists"
                        response = {'msg':msg, 'success':success}
                        return HttpResponse(json.dumps(response), mimetype = "application/json")
                    else:
                        desig_obj_list[0].active = 2
                        desig_obj_list[0].save()
                else:
                    form.save()
                added = True
                msg = "Designation added successfully"
                success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        designation_obj = Designation.objects.get(id=id_edit)
        form = add_designation_form(instance=designation_obj)
        if request.method == 'POST':
            form = add_designation_form(request.POST, instance=designation_obj)
            if form.is_valid():
                dept_obj_list = Designation.objects.filter(name = request.POST.get('name',"")).exclude(id=int(id_edit))
                if dept_obj_list:
                    msg = "Designation already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Designation edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="delete":
        id_del = request.GET.get('id_del')
        designation = Designation.objects.get(id = id_del)
        designation.active = 0
        designation.save()
        msg = "Designation deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        designation = Designation.objects.get(id = active)
        designation.active = 2
        designation.save()
        msg = "Designation activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_designation.html', locals(), context_instance = RequestContext(request))


def manage_skills(request, task=None):

    """ Designation record management funtions """
    response = {}
    success = False
    msg = ''

    if task == "add":
        form = add_skills_form()
        if request.method == "POST":
            form = add_skills_form(request.POST)
            if form.is_valid():
                skill_type_obj = Skill_Type.objects.get(id = int(request.POST.get('skill_type')))
                skills_obj_list = Skills.objects.filter(skill_type = skill_type_obj, name__iexact= request.POST.get('name', ""))
                if skills_obj_list:
                    if skills_obj_list[0].active == 2:
                        msg = "Skill with this name already exists"
                        response = {'msg':msg, 'success':success}
                        return HttpResponse(json.dumps(response), mimetype = "application/json")
                    else:
                        skills_obj_list[0].active = 2
                        skills_obj_list[0].save()
                else:
                    form.save()
                added = True
                msg = "Skill added successfully"
                success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")


    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        skill_obj = Skills.objects.get(id=id_edit)
        form = add_skills_form(instance=skill_obj)
        if request.method == 'POST':
            form = add_skills_form(request.POST, instance=skill_obj)
            if form.is_valid():
                skill_type_obj = Skill_Type.objects.get(id = int(request.POST.get('skill_type')))
                skill  = Skills.objects.filter(skill_type=skill_type_obj, name__iexact = request.POST.get('name',"")).exclude(id=int(id_edit))
                if skill :
                    msg = "Skill type with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Skill edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="delete":
        id_del = request.GET.get('id_del')
        skill = Skills.objects.get(id = id_del)
        skill.active = 0
        skill.save()
        msg = "Skill deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        skill = Skills.objects.get(id = active)
        skill.active = 2
        skill.save()
        msg = "Skill activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_skill.html', locals(), context_instance = RequestContext(request))


def manage_skill_type(request, task=None):

    """ Designation record management funtions """
    response = {}
    success = False
    msg = ''

    if task == "add":
        form = add_skill_type_form()
        if request.method == "POST":
            form = add_skill_type_form(request.POST)
            if form.is_valid():
                skill_type_list = Skill_Type.objects.filter(name__iexact= request.POST.get('name', ""))
                if skill_type_list:
                    if skill_type_list[0].active == 2:
                        msg = "Skill type with this name already exists"
                        response = {'msg':msg, 'success':success}
                        return HttpResponse(json.dumps(response), mimetype = "application/json")
                    else:
                        skill_type_list[0].active == 2
                        skill_type_list[0].save()
                else:
                    form.save()
                added = True
                msg = "Skill type added successfully"
                success = True
            else:
                msg = "Error Occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        skill_type_obj = Skill_Type.objects.get(id=id_edit)
        form = add_skill_type_form(instance=skill_type_obj)
        if request.method == 'POST':
            form = add_skill_type_form(request.POST, instance=skill_type_obj)
            if form.is_valid():
                skill_type  = Skill_Type.objects.filter(name__iexact= request.POST.get('name',"")).exclude(id=int(id_edit))
                if skill_type :
                    msg = "Skill type with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Skill type edited successfully"
                    success = True
            else:
                msg = "Invalid form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="delete":
        id_del = request.GET.get('id_del')
        skill_type = Skill_Type.objects.get(id = id_del)
        skill_type.active = 0
        skill_type.save()
        msg = "Skill type deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        skill_type = Skill_Type.objects.get(id = active)
        skill_type.active = 2
        skill_type.save()
        msg = "Skill type activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_skill_type.html', locals(), context_instance = RequestContext(request))

def manage_staff_type(request, task=None):

    """ Designation record management funtions """
    response = {}
    success = False
    msg = ''

    if task == "add":
        form = add_staff_type_form()
        if request.method == "POST":
            form = add_staff_type_form(request.POST)
            if form.is_valid():
                staff_type_list = Staff_Type.objects.filter(name__iexact= request.POST.get('name', ""))
                if staff_type_list:
                    if staff_type_list[0].active == 2:
                        msg = "Staff type with this name already exists"
                        response = {'msg':msg, 'success':success}
                        return HttpResponse(json.dumps(response), mimetype = "application/json")
                    else:
                        staff_type_list[0].active == 2
                        staff_type_list[0].save()
                else:
                    form.save()
                added = True
                msg = "Staff type added successfully"
                success = True
            else:
                msg = "Error occurred"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")


    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        staff_type_obj = Staff_Type.objects.get(id=id_edit)
        form = add_staff_type_form(instance=staff_type_obj)
        if request.method == 'POST':
            form = add_staff_type_form(request.POST, instance=staff_type_obj)
            if form.is_valid():
                staff_type  = Staff_Type.objects.filter(name__iexact= request.POST.get('name',"")).exclude(id=int(id_edit))
                if staff_type :
                    msg = "Staff type with this name already exists"
                else:
                    form.save()
                    edit_done = True
                    msg = "Staff type edited successfully"
                    success = True
            else:
                msg = "Invalid Form"
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="delete":
        id_del = request.GET.get('id_del')
        staff_type = Staff_Type.objects.get(id = id_del)
        staff_type.active = 0
        staff_type.save()
        msg = "Staff type deactivated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task == "active":
        active = request.GET.get('active')
        staff_type = Staff_Type.objects.get(id = active)
        staff_type.active = 2
        staff_type.save()
        msg = "Staff type activated successfully"
        success = True
        response = {'msg':msg, 'success':success}
        return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_staff_type.html', locals(), context_instance = RequestContext(request))


def manage_salary(request, task=None):

    """ Designation record management funtions """
    response = {}
    success = False
    msg = ''

    if task == "add":

        form = form = add_salary_form()
        if request.method == "POST":
            form = add_salary_form(request.POST)
            if form.is_valid():
                form2 = form.save(commit=False)
                form2.added_by = request.user
                form2.save()
                added = True
                msg = "Salary added successfully"
                success = True
            else:
                msg = "Error occurred"
                if form.non_field_errors():
                    msg = [i for i in form.non_field_errors()]
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        salary_obj = Salary.objects.get(id=id_edit)
        form = add_salary_form(instance=salary_obj)
        if request.method == 'POST':
            form = add_salary_form(request.POST, instance=salary_obj)
            if form.is_valid():
                form.save()
                edit_done = True
                msg = "Salary edited successfully"
                success = True
            else:
                msg = "Invalid Form"
                if form.non_field_errors():
                    msg = [i for i in form.non_field_errors()]
                if form.errors:
                    msg = form.errors.keys() + " : " + form.errors.values()
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_salary.html', locals(), context_instance = RequestContext(request))

def manage_payment(request, task=None):

    """ Payment record management funtions """
    response = {}
    success = False
    msg = ''
    if task == "add":
        staff_id = int(request.GET.get('staff_id'))
        form = cus_pay_salary_form(staff_id)
        if request.method == "POST":
            staff_obj = Staff.objects.get(id=staff_id)
            form = form(request.POST)
            if form.is_valid():
                form2 = form.save(commit=False)
                form2.added_by = request.user
                form2.staff = staff_obj
                form2.save()
                added = True
                msg = "Payment added successfully"
                success = True
            else:
                msg = "Error Occurred"
                if form.non_field_errors():
                    msg = form.non_field_errors()[0]
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    elif task =="edit":
        id_edit = request.GET.get('id_edit')
        salary_obj = Paid_Salary.objects.get(id=int(id_edit))
        staff_id = salary_obj.staff.id # staff_id if required in template
        form2 = cus_pay_salary_form(salary_obj.staff.id)
        form = form2(instance=salary_obj)
        if request.method == 'POST':
            form = form2(request.POST, instance=salary_obj)
            if form.is_valid():
                form.save()
                edit_done = True
                msg = "Payment edited successfully"
                success = True
            else:
                msg = [i for i in form.non_field_errors()]
            response = {'msg':msg, 'success':success}
            return HttpResponse(json.dumps(response), mimetype = "application/json")

    return render_to_response('hrmanagement/add_edit_payment.html', locals(), context_instance = RequestContext(request))

def payment_details(request, task=None):

    """ Payment details management funtions """
    staff_id = request.GET['staff_id']
    staff_obj = Staff.objects.get(id=int(staff_id))
    item_list = Paid_Salary.objects.filter(staff = staff_obj)
    key = 'payment'
    title = 'Payment'
    return render_to_response('hrmanagement/master_replace.html', locals(), context_instance = RequestContext(request))


def salary_details(request):
    staff_id = request.GET['staff_id']
    staff_obj = Staff.objects.get(id=int(staff_id))
    item_list = Paid_Salary.objects.filter(staff = staff_obj)
    return render(request, 'hrmanagement/list_salary_details.html', locals())


def edit_salary(request, salary_id=""):

    errors = {}
    salary_obj = Salary.objects.get(id=salary_id)
    if request.method == "POST":
        form = add_salary_form(request.POST, instance=salary_obj)
        if form.is_valid():
            form.save()
            record_updated = True
    else:
        form = add_salary_form(instance=salary_obj)
    return render(request, 'hrmanagement/add_edit_salary.html', locals())


import json
def get_county(request):

    if request.is_ajax():
        results = {}
        state_id = int(request.GET.get('state_id'))
        from farmer.models import Boundary
        try:
              state_obj = Boundary.objects.get(id=state_id)
              county_list = Boundary.objects.filter(parent=state_obj).values('id','name')
              #sg_list = StudentGroup.objects.filter(institution = ins_obj , stream = stream_obj).values('id','name')
        except Exception:
            pass
        results['res'] = [i for i in county_list]
        return HttpResponse(json.dumps(results), mimetype = 'application/json')
