"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from hrmanagement.models import *
from farmer.models import *
from django.forms.fields import DateField


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class Master_Data(TestCase):
    def test_insert_master_data(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        d = DateField()
        joining_date = d.to_python('2014-02-02')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)

    def test_invalid_master_data(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_typ, personal_info=person, date_of_joining=joining_date, work_experience=2)

    def test_list_staff(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_all_staff()[0].personal_info.first_name, "harish")

    def test_get_staff_address(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_staff_address().count(), 1)

    def test_get_staff_address1(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_staff_address().count(), 5)

    def test_get_staff_type(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff_type.get_all_staff().count(),1)

    def test_get_staff_type1(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff_type.get_all_staff().count(),3)

class Data(TestCase):
    def test_insert(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        d = DateField()
        joining_date = d.to_python('2014-02-02')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)

    def test_invalid_data(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_typ, personal_info=person, date_of_joining=joining_date, work_experience=2)


    def test_list(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_all_staff()[0].personal_info.first_name, "harish")

    def test_list1(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_all_staff()[0].personal_info.first_name, "harish11")

    def test_get_staff1_address(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_staff_address().count(),1)

    def test_get_staff1_address1(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff.get_staff_address().count(),3)

    def test_get_staff2_type(self):
        department = Department.objects.create(name="agriculture")
        designation = Designation.objects.create(name="jr_teacher")
        skill_type = Skill_Type.objects.create(name = "teaching")
        position_type = Position_Type.objects.create(name = "senior")
        salutions = Salutations.objects.create(name = "Dr")
        maritial_status = Maritial_Status.objects.create(name = "married")
        skill = Skills.objects.create(skill_type = skill_type, name="botany")
        staff_type = Staff_Type.objects.create(name="Worker")
        person = Person.objects.create(position_type=position_type, prefix = salutions, first_name = 'harish',farmer_id = '123',gender = 'male',maritial_status= maritial_status, uuid = 'sdf45')
        from datetime import datetime
        joining_date = datetime.strptime('2008-12-12', '%Y-%m-%d')
        staff = Staff.objects.create(staff_type=staff_type, personal_info=person, date_of_joining=joining_date, work_experience=2)
        self.assertEqual(staff_type.get_all_staff().count(),1)
