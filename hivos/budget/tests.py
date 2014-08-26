"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from budget.models import *
class Activity_status1(TestCase):

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
        self.assertEqual(act_list.name,'In ')

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

class t_budget(TestCase):

    def test_add(self):
        Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        st_list = Budget.objects.all()
        self.assertEqual(st_list.count(), 1)

    def test_update(self):
        Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        act_list = Budget.objects.get(title='dsaf')
        act_list.title = 'aaa'
        act_list.save()
        self.assertEqual(act_list.title,'aaa')

    def test_update1(self):
        Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        act_list = Budget.objects.get(title='dsaf')
        act_list.title = 'aaa'
        act_list.save()
        self.assertEqual(act_list.title,'bbb')

    def test_delete(self):

        Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        act_list = Budget.objects.get(title='dsaf')
        act_list.active = 0
        act_list.save()
        act_list = Budget.objects.filter(active=2)
        self.assertEqual(act_list.count(), 0)

    def test_delete1(self):

        Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        act_list = Budget.objects.get(title='dsaf')
        act_list.active = 0
        act_list.save()
        act_list = Budget.objects.filter(active=2)
        self.assertEqual(act_list.count(), 2)

class Budget_Strategy1(TestCase):

    def test_add(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        st_list = Budget_Strategy.objects.all()
        self.assertEqual(st_list.count(), 1)

    def test_update(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_list = Budget_Strategy.objects.get(title='st1')
        act_list.title = 'In progress'
        act_list.save()
        self.assertEqual(act_list.title,'In progress')

    def test_update1(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_list = Budget_Strategy.objects.get(title='st1')
        act_list.title = 'In progress'
        act_list.save()
        self.assertEqual(act_list.title,'ffff')

    def test_delete(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_list = Budget_Strategy.objects.get(title='st1')
        act_list.active = 0
        act_list.save()
        st_list = Budget_Strategy.objects.filter(active=2)
        self.assertEqual(st_list.count(), 0)

    def test_delete1(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_list = Budget_Strategy.objects.get(title='st1')
        act_list.active = 0
        act_list.save()
        st_list = Budget_Strategy.objects.filter(active=2)
        self.assertEqual(st_list.count(), 5)

class budget_activity1(TestCase):

    def test_add(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        bud_st = Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_st = Activity_Status.objects.create(name='completed')
        Budget_Activity.objects.create(title="act1",budget=bud_obj, status=act_st)
        b_list = Budget.objects.all()
        self.assertEqual(b_list.count(), 1)

    def test_update(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        bud_st = Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_st = Activity_Status.objects.create(name='completed')
        Budget_Activity.objects.create(title="act1",budget=bud_obj, status=act_st)
        b_obj = Budget.objects.get(id=1)
        b_obj.title = "budget12"
        b_obj.save()
        b_list = Budget.objects.get(id=1)
        self.assertEqual(b_list.title, "budget12")

    def test_update1(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        bud_st = Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_st = Activity_Status.objects.create(name='completed')
        Budget_Activity.objects.create(title="act1",budget=bud_obj, status=act_st)
        b_obj = Budget.objects.get(id=1)
        b_obj.title = "budget12"
        b_obj.save()
        b_list = Budget.objects.get(id=1)
        self.assertEqual(b_list.title, "budget")

    def test_delete(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        bud_st = Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_st = Activity_Status.objects.create(name='completed')
        Budget_Activity.objects.create(title="act1",budget=bud_obj, status=act_st)
        b_obj = Budget.objects.get(id=1)
        b_obj.active = 0
        b_obj.save()
        b_list = Budget.objects.filter(active=2)
        self.assertEqual(b_list.count(), 0)

    def test_delete1(self):
        bud_obj = Budget.objects.create(title="dsaf",start_date="2012-02-02", end_date="2012-02-03", budget=200,description="dsfg")
        bud_st = Budget_Strategy.objects.create(title="st1",budget=bud_obj, description="dsfas")
        act_st = Activity_Status.objects.create(name='completed')
        Budget_Activity.objects.create(title="act1",budget=bud_obj, status=act_st)
        b_obj = Budget.objects.get(id=1)
        b_obj.active = 0
        b_obj.save()
        b_list = Budget.objects.filter(active=2)
        self.assertEqual(b_list.count(), 10)

