"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from farmer.models import *
from mastermodule.models import *
from django.test import Client
from django.contrib.contenttypes.models import ContentType

from django.test import TestCase
from projects.models import *

class activity_status1(TestCase):

    def test_add(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.all()
        self.assertEqual(act_list.count(), 1)

    def test_update(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.get(name='completed')
        act_list.name = 'In progress'
        act_list.save()
        self.assertEqual(act_list.name,'In progress')

    def test_delete(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.get(name='completed')
        act_list.active = 0
        act_list.save()
        act_list = Activity_Status.objects.filter(active=2)
        self.assertEqual(act_list.count(), 0)

class coordinator_type(TestCase):

    def test_add(self):
        Coordinator_Type.objects.create(name='head')
        ct_list = Coordinator_Type.objects.all()
        self.assertEqual(ct_list.count(), 1)

    def test_update(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.name = 'president'
        ct_obj.save()
        self.assertEqual(ct_obj.name, 'president')

    def test_update1(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.name = 'president'
        ct_obj.save()
        self.assertEqual(ct_obj.name, 'pres')

    def test_delete(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.active=0
        ct_obj.save()
        ct_list = Coordinator_Type.objects.filter(active=2)
        self.assertEqual(ct_list.count(), 0)

    def test_delete1(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.active=0
        ct_obj.save()
        ct_list = Coordinator_Type.objects.filter(active=2)
        self.assertEqual(ct_list.count(), 2)


class project_type(TestCase):

    def test_add(self):
        Project_Type.objects.create(name="agri")
        pt_list = Project_Type.objects.all()
        self.assertEqual(pt_list.count(), 1)

    def test_update(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.name = "cattle"
        pt_obj.save()
        self.assertEqual(pt_obj.name, 'cattle')

    def test_update1(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.name = "cattle"
        pt_obj.save()
        self.assertEqual(pt_obj.name, 'cat')

    def test_delete(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.active = 0
        pt_obj.save()
        pt_list = Project_Type.objects.filter(active=2)
        self.assertEqual(pt_list.count(), 0)

    def test_delete1(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.active = 0
        pt_obj.save()
        pt_list = Project_Type.objects.filter(active=2)
        self.assertEqual(pt_list.count(), 2)

class project(TestCase):

    def test_add(self):
        activity_st_obj = Activity_Status.objects.create(name='completed')
        coordinator_type_obj = Coordinator_Type.objects.create(name='head')
        project_type_obj = Project_Type.objects.create(name="agri")
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_list = Project.objects.all()
        self.assertEqual(project_list.count(), 1)

    def test_update(self):
        activity_st_obj = Activity_Status.objects.create(name='completed')
        coordinator_type_obj = Coordinator_Type.objects.create(name='head')
        project_type_obj = Project_Type.objects.create(name="agri")
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.name = "feeds management"
        project_obj.save()
        self.assertEqual(project_obj.name, 'feeds management')

    def test_update1(self):
        activity_st_obj = Activity_Status.objects.create(name='completed')
        coordinator_type_obj = Coordinator_Type.objects.create(name='head')
        project_type_obj = Project_Type.objects.create(name="agri")
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.name = "feeds management"
        project_obj.save()
        self.assertEqual(project_obj.name, 'feeds ')


class activity_status(TestCase):

    def test_add(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.all()
        self.assertEqual(act_list.count(), 1)

    def test_update(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.get(name='completed')
        act_list.name = 'In progress'
        act_list.save()
        self.assertEqual(act_list.name,'In progress')

    def test_update1(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.get(name='completed')
        act_list.name = 'In progress'
        act_list.save()
        self.assertEqual(act_list.name,'In')

    def test_delete(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.get(name='completed')
        act_list.active = 0
        act_list.save()
        act_list = Activity_Status.objects.filter(active=2)
        self.assertEqual(act_list.count(), 0)

    def test_delete1(self):
        Activity_Status.objects.create(name='completed')
        act_list = Activity_Status.objects.get(name='completed')
        act_list.active = 0
        act_list.save()
        act_list = Activity_Status.objects.filter(active=2)
        self.assertEqual(act_list.count(), 1)

class coordinator_type(TestCase):

    def test_add(self):
        Coordinator_Type.objects.create(name='head')
        ct_list = Coordinator_Type.objects.all()
        self.assertEqual(ct_list.count(), 1)

    def test_update(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.name = 'president'
        ct_obj.save()
        self.assertEqual(ct_obj.name, 'president')

    def test_update1(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.name = 'president'
        ct_obj.save()
        self.assertEqual(ct_obj.name, 'pres')

    def test_delete(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.active=0
        ct_obj.save()
        ct_list = Coordinator_Type.objects.filter(active=2)
        self.assertEqual(ct_list.count(), 0)

    def test_delete1(self):
        ct_obj = Coordinator_Type.objects.create(name='head')
        ct_obj.active=0
        ct_obj.save()
        ct_list = Coordinator_Type.objects.filter(active=2)
        self.assertEqual(ct_list.count(), 1)

class project_type(TestCase):

    def test_add(self):
        Project_Type.objects.create(name="agri")
        pt_list = Project_Type.objects.all()
        self.assertEqual(pt_list.count(), 1)

    def test_update(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.name = "cattle"
        pt_obj.save()
        self.assertEqual(pt_obj.name, 'cattle')

    def test_update1(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.name = "cattle"
        pt_obj.save()
        self.assertEqual(pt_obj.name, 'catt')

    def test_delete(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.active = 0
        pt_obj.save()
        pt_list = Project_Type.objects.filter(active=2)
        self.assertEqual(pt_list.count(), 0)

    def test_delete1(self):
        pt_obj = Project_Type.objects.create(name="agri")
        pt_obj.active = 0
        pt_obj.save()
        pt_list = Project_Type.objects.filter(active=2)
        self.assertEqual(pt_list.count(), 1)

class project(TestCase):

    def test_add(self):
        activity_st_obj = Activity_Status.objects.create(name='completed')
        coordinator_type_obj = Coordinator_Type.objects.create(name='head')
        project_type_obj = Project_Type.objects.create(name="agri")
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_list = Project.objects.all()
        self.assertEqual(project_list.count(), 1)

    def test_update(self):
        activity_st_obj = Activity_Status.objects.create(name='completed')
        coordinator_type_obj = Coordinator_Type.objects.create(name='head')
        project_type_obj = Project_Type.objects.create(name="agri")
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.name = "feeds management"
        project_obj.save()
        self.assertEqual(project_obj.name, 'feeds management')

    def test_update1(self):
        activity_st_obj = Activity_Status.objects.create(name='completed')
        coordinator_type_obj = Coordinator_Type.objects.create(name='head')
        project_type_obj = Project_Type.objects.create(name="agri")
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.name = "feeds management"
        project_obj.save()
        self.assertEqual(project_obj.name, 'feeds')


class SimpleTest11(TestCase):

    def test_add_project(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        group_obj = Group.objects.create(name='group1',date_of_formation='2014-02-05', group_size=10)
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.groups.add(group_obj)
        resp1 = client1.post('/projects/project/add/',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_project(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        group_obj = Group.objects.create(name='group1',date_of_formation='2014-02-05', group_size=10)
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)

        project_obj.groups.add(group_obj)
        group_obj1 = Group.objects.create(name='group2',date_of_formation='2014-02-05', group_size=10)
        project_obj.groups.add(group_obj1)
        proj_obj = Project.objects.get(id=project_obj.id)
        proj_obj.name = 'Project1'
        proj_obj.save()
        #group_obj1.save()
        resp1 = client1.post('/projects/project/edit/?id_edit=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_project1(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        group_obj = Group.objects.create(name='group1',date_of_formation='2014-02-05', group_size=10)
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)

        project_obj.groups.add(group_obj)
        group_obj1 = Group.objects.create(name='group2',date_of_formation='2014-02-05', group_size=10)
        project_obj.groups.add(group_obj1)
        proj_obj = Project.objects.get(id=project_obj.id)
        proj_obj.name = 'Project1'
        proj_obj.save()
        #group_obj1.save()
        resp1 = client1.post('/projects/project/edit/?id_edit=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_delete_project(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        group_obj = Group.objects.create(name='group1',date_of_formation='2014-02-05', group_size=10)
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.groups.add(group_obj)
        proj_obj = Project.objects.get(id=project_obj.id)
        proj_obj.active = 0
        proj_obj.save()
        resp1 = client1.post('/projects/project/delete/?id_del=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_project(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        group_obj = Group.objects.create(name='group1',date_of_formation='2014-02-05', group_size=10)
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        project_obj.groups.add(group_obj)
        proj_obj = Project.objects.get(id=project_obj.id)
        proj_obj.active = 2
        proj_obj.save()
        resp1 = client1.post('/projects/project/active/?active=1',{})
        self.assertEqual(resp1.status_code,200)

class ProjectCoordinator(TestCase):
    def test_add_projectcordinator(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        safftype_obj = Staff_Type.objects.create(name='Head')
        salutation_obj = Salutations.objects.create(name='Mr')
        marital_obj = Maritial_Status.objects.create(name='Single')
        person_obj = Person.objects.create(prefix=salutation_obj, maritial_status=marital_obj)
        staff_obj = Staff.objects.create(staff_type=safftype_obj,personal_info=person_obj,date_of_joining='2014-03-05',date_of_leaving='2014-03-06',work_experience=2.5)
        coordinator_obj = Coordinator_Type.objects.create(name='coordinator1')
        projctcoordinator_obj = Project_Coordinators.objects.create(project=project_obj,staff=staff_obj,coordinator_type= coordinator_obj)
        resp1 = client1.post('/projects/coordinator/add/',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_projectcordinator(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        safftype_obj = Staff_Type.objects.create(name='Head')
        salutation_obj = Salutations.objects.create(name='Mr')
        marital_obj = Maritial_Status.objects.create(name='Single')
        person_obj = Person.objects.create(prefix=salutation_obj, maritial_status=marital_obj)
        staff_obj = Staff.objects.create(staff_type=safftype_obj,personal_info=person_obj,date_of_joining='2014-03-05',date_of_leaving='2014-03-06',work_experience=2.5)
        coordinator_obj = Coordinator_Type.objects.create(name='coordinator1')
        projctcoordinator_obj = Project_Coordinators.objects.create(project=project_obj,staff=staff_obj,coordinator_type= coordinator_obj)
        cordinator_obj = Coordinator_Type.objects.get(id= coordinator_obj.id)
        maritial_obj = Maritial_Status.objects.get(id=marital_obj.id)
        cordinator_obj.name = 'Cordinator2'
        maritial_obj.name = 'Married'
        cordinator_obj.save()
        maritial_obj.save()
        projctcoordinator_obj.save()
        resp1 = client1.post('/projects/coordinator/edit/?id_edit=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_delete_projectcordinator(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        safftype_obj = Staff_Type.objects.create(name='Head')
        salutation_obj = Salutations.objects.create(name='Mr')
        marital_obj = Maritial_Status.objects.create(name='Single')
        person_obj = Person.objects.create(prefix=salutation_obj, maritial_status=marital_obj)
        staff_obj = Staff.objects.create(staff_type=safftype_obj,personal_info=person_obj,date_of_joining='2014-03-05',date_of_leaving='2014-03-06',work_experience=2.5)
        coordinator_obj = Coordinator_Type.objects.create(name='coordinator1')
        projctcoordinator_obj = Project_Coordinators.objects.create(project=project_obj,staff=staff_obj,coordinator_type= coordinator_obj)
        projectco_obj = Project_Coordinators.objects.get(id= projctcoordinator_obj.id)
        projectco_obj.active = 0
        projectco_obj.save()
        resp1 = client1.post('/projects/coordinator/delete/?id_del=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_projectcordinator(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        safftype_obj = Staff_Type.objects.create(name='Head')
        salutation_obj = Salutations.objects.create(name='Mr')
        marital_obj = Maritial_Status.objects.create(name='Single')
        person_obj = Person.objects.create(prefix=salutation_obj, maritial_status=marital_obj)
        staff_obj = Staff.objects.create(staff_type=safftype_obj,personal_info=person_obj,date_of_joining='2014-03-05',date_of_leaving='2014-03-06',work_experience=2.5)
        coordinator_obj = Coordinator_Type.objects.create(name='coordinator1')
        projctcoordinator_obj = Project_Coordinators.objects.create(project=project_obj,staff=staff_obj,coordinator_type= coordinator_obj)
        projectco_obj = Project_Coordinators.objects.get(id= projctcoordinator_obj.id)
        projectco_obj.active = 2
        projectco_obj.save()
        resp1 = client1.post('/projects/coordinator/active/?active=1',{})
        self.assertEqual(resp1.status_code,200)

class BudgetHead(TestCase):
    def test_add_budget(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project = project_obj,name = 'name1',description = 'fghjh')
        resp1 = client1.post('/projects/budget-head/add/',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_budget(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project = project_obj,name = 'name1',description = 'fghjh')
        protype_obj =  Project_Type.objects.get(id = project_type_obj.id)
        budget_obj = Budget_Head.objects.get(id = budgethead_obj.id)
        protype_obj.name = 'cattlefield'
        budget_obj.name = 'name2'
        protype_obj.save()
        budget_obj.save()
        budgethead_obj.save()
        resp1 = client1.post('/projects/budget-head/edit/?id_edit=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_delete_budget(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project = project_obj,name = 'name1',description = 'fghjh')
        budget_obj = Budget_Head.objects.get(id = budgethead_obj.id)
        budget_obj.active = 0
        budget_obj.save()
        resp1 = client1.post('/projects/budget-head/delete/?id_del=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_budget(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project = project_obj,name = 'name1',description = 'fghjh')
        budget_obj = Budget_Head.objects.get(id = budgethead_obj.id)
        budget_obj.active = 2
        budget_obj.save()
        resp1 = client1.post('/projects/budget-head/active/?active=1',{})
        self.assertEqual(resp1.status_code,200)

class MileStone(TestCase):
    def test_add_milestone(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        milestone_obj = Milestone.objects.create(project =project_obj,title ='ghbjn',description='gjk')
        resp1 = client1.post('/projects/milestone/add/',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_milestone(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        milestone_obj = Milestone.objects.create(project =project_obj,title ='ghbjn',description='gjk')
        protype_obj = Project_Type.objects.get(id = project_type_obj.id)
        mile_obj =  Milestone.objects.get(id = milestone_obj.id)
        protype_obj.name= 'cattlefield'
        mile_obj.title='Mj5'
        protype_obj.save()
        mile_obj.save()
        resp1 = client1.post('/projects/milestone/edit/?id_edit=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_delete_milestone(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        milestone_obj = Milestone.objects.create(project =project_obj,title ='ghbjn',description='gjk')
        mile_obj =  Milestone.objects.get(id = milestone_obj.id)
        mile_obj.active = 0
        mile_obj.save()
        resp1 = client1.post('/projects/milestone/delete/?id_del=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_milestone(self):
        client1 = Client()
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        milestone_obj = Milestone.objects.create(project =project_obj,title ='ghbjn',description='gjk')
        mile_obj =  Milestone.objects.get(id = milestone_obj.id)
        mile_obj.active = 2
        mile_obj.save()
        resp1 = client1.post('/projects/milestone/active/?active=1',{})
        self.assertEqual(resp1.status_code,200)

class Training(TestCase):
    def test_add_training(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        #ctype_mile = ContentType.objects.get(app_label="projects",model__iexact='Milestone')
        prog_obj = Program.objects.create(title='cvhj',start_date='2013-02-03',end_date='2014-02-03')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Training
        #import ipdb;ipdb.set_trace()
        training1_ob = Training.objects.create(content_type=ctype,object_id = 1,program=prog_obj)
        resp1 = client1.post('/projects/training/add/?project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_training(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        prog_obj = Program.objects.create(title='cvhj',start_date='2013-02-03',end_date='2014-02-03')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Training
        #import ipdb;ipdb.set_trace()
        training1_ob = Training.objects.create(content_type=ctype,object_id = 1,program=prog_obj)
        proj_obj = Project.objects.get(id =  project_obj.id)
        program_obj = Program.objects.get(id = prog_obj.id)
        program_obj.title ='ami'
        program_obj.save()
        resp1 = client1.post('/projects/training/edit/?id_edit=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)


    def test_delete_training(self):
        client1 = Client()

        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        prog_obj = Program.objects.create(title='cvhj',start_date='2013-02-03',end_date='2014-02-03')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Training

        training1_ob = Training.objects.create(content_type=ctype,object_id = 1,program=prog_obj)
        training_obj = Training.objects.get(id = training1_ob.id)
        training_obj.active = 0
        training_obj.save()
        resp1 = client1.post('/projects/training/delete/?id_del=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_training(self):
        client1 = Client()

        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        prog_obj = Program.objects.create(title='cvhj',start_date='2013-02-03',end_date='2014-02-03')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Training

        training1_ob = Training.objects.create(content_type=ctype,object_id = 1,program=prog_obj)
        training_obj = Training.objects.get(id = training1_ob.id)
        training_obj.active = 0
        training_obj.save()
        resp1 = client1.post('/projects/training/active/?active=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

class Strategy(TestCase):
    def test_add_strategy(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Strategy
        strategy_obj = Strategy.objects.create(content_type=ctype,object_id = 1,title='cvhc',description='jusjdiu')
        resp1 = client1.post('/projects/strategy/add/?project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_strategy(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Strategy
        strategy_obj = Strategy.objects.create(content_type=ctype,object_id = 1,title='cvhc',description='jusjdiu')
        strat_obj = Strategy.objects.get(id = strategy_obj.id)
        strat_obj.title='asua'
        strat_obj.save()
        resp1 = client1.post('/projects/strategy/edit/?id_edit=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_strategy(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Strategy
        strategy_obj = Strategy.objects.create(content_type=ctype,object_id = 1,title='cvhc',description='jusjdiu')
        strat_obj = Strategy.objects.get(id = strategy_obj.id)
        strat_obj.active=0
        strat_obj.save()
        resp1 = client1.post('/projects/strategy/delete/?id_del=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_strategy(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        from projects.models import Strategy
        strategy_obj = Strategy.objects.create(content_type=ctype,object_id = 1,title='cvhc',description='jusjdiu')
        strat_obj = Strategy.objects.get(id = strategy_obj.id)
        strat_obj.active=2
        strat_obj.save()
        resp1 = client1.post('/projects/strategy/active/?active=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

class ProjectActivity(TestCase):
    def test_add_activity(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Milestone')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        milestone_obj = Milestone.objects.create(title='fggh',description='xs',project=project_obj)
        budgethead_obj = Budget_Head.objects.create(project=project_obj,name='Head1')
        activitystat_obj = Activity_Status.objects.create(name='In process')
        activitype_obj = Activity_Type.objects.create(name='Activity Type1')
        activity_obj = Activity.objects.create(content_type=ctype,object_id=1,budget_head=budgethead_obj,activity_type=activitype_obj,status=activitystat_obj,budget=2000.0)
        resp1 = client1.post('/projects/activity/add/?milestone_id=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_edit_activity(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project=project_obj,name='Head1')
        activitystat_obj = Activity_Status.objects.create(name='In process')
        activitype_obj = Activity_Type.objects.create(name='Activity Type1')
        activity_obj = Activity.objects.create(content_type=ctype,object_id=1,budget_head=budgethead_obj,activity_type=activitype_obj,status=activitystat_obj,budget=2000.0)
        actsat_obj = Activity_Status.objects.get(id = activitystat_obj.id )
        actsat_obj.name='Closed'
        actsat_obj.save()
        resp1 = client1.post('/projects/activity/edit/?id_edit=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_delete_activity(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project=project_obj,name='Head1')
        activitystat_obj = Activity_Status.objects.create(name='In process')
        activitype_obj = Activity_Type.objects.create(name='Activity Type1')
        activity_obj = Activity.objects.create(content_type=ctype,object_id=1,budget_head=budgethead_obj,activity_type=activitype_obj,status=activitystat_obj,budget=2000.0)
        act_obj = Activity.objects.get(id = activity_obj.id )
        act_obj.active=0
        act_obj.save()
        resp1 = client1.post('/projects/activity/delete/?id_del=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)

    def test_active_activity(self):
        client1 = Client()
        ctype=ContentType.objects.get(app_label="projects",model__iexact='Project')
        project_type_obj = Project_Type.objects.create(name="agri")
        activity_st_obj = Activity_Status.objects.create(name='completed')
        project_obj = Project.objects.create(project_type=project_type_obj, name='cattle management', budget=2123, status=activity_st_obj)
        budgethead_obj = Budget_Head.objects.create(project=project_obj,name='Head1')
        activitystat_obj = Activity_Status.objects.create(name='In process')
        activitype_obj = Activity_Type.objects.create(name='Activity Type1')
        activity_obj = Activity.objects.create(content_type=ctype,object_id=1,budget_head=budgethead_obj,activity_type=activitype_obj,status=activitystat_obj,budget=2000.0)
        act_obj = Activity.objects.get(id = activity_obj.id )
        act_obj.active=2
        act_obj.save()
        resp1 = client1.post('/projects/activity/active/?active=1&project_id=1',{})
        self.assertEqual(resp1.status_code,200)