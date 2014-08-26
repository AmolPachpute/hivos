from farmer.models import Common_Info, Salutations, Maritial_Status, Boundary, \
Educational_Qualification
from django.db import models
from farmer.thumbs import ImageWithThumbsField
from farmer.models import *
from django.contrib.auth.models import User

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^farmer\.thumbs\.ImageWithThumbsField"])

GENDER_CHOICES = (('male', 'male'), ('female', 'female'), ('other', 'other'))

class Department(Common_Info):
    name = models.CharField('Name*', max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

    def get_all_staff(self):
        return Staff.objects.filter(department=self,active=2)

class Designation(Common_Info):
    name = models.CharField('Name*', max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

    def get_all_staff(self):
        return Staff.objects.filter(designation=self,active=2)


class Skill_Type(Common_Info):
    name = models.CharField('Name*', max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

class Skills(Common_Info):
    skill_type = models.ForeignKey(Skill_Type, verbose_name='Skill Type*')
    name = models.CharField('Name*', max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

class Staff_Type(Common_Info):
    name = models.CharField('Name*', max_length=100)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return self.name

    def get_all_staff(self):
        return Staff.objects.filter(staff_type=self,active=2)

from farmer.models import Person
class Staff(Common_Info):
    staff_type = models.ForeignKey(Staff_Type, verbose_name='Staff Type*')
    personal_info = models.ForeignKey(Person)
    skills = models.ManyToManyField(Skills,blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True)
    designation = models.ForeignKey(Designation, blank=True, null=True)
    qualification = models.ManyToManyField(Educational_Qualification, blank=True, null=True)
    date_of_joining = models.DateField('Joining Date*')
    date_of_leaving = models.DateField(blank=True, null=True)
    photo = ImageWithThumbsField(upload_to='static/%Y/%m/%d', sizes=((90, 120), ((120, 118)), (180, 240), (360, 480)), blank=True, null=True)
    work_experience = models.DecimalField('Work Experience*(In Years)', decimal_places=6, max_digits=10)
    active = models.IntegerField(default=2)

    def __unicode__(self):
        return '%s %s %s ' % (self.personal_info.first_name, self.personal_info.middle_name, self.personal_info.Last_name)

    def get_staff_address(self):
        return Staff_Address.objects.filter(staff=self)

class Staff_Address(Common_Info):
    staff = models.ForeignKey(Staff, verbose_name="Staff*")
    address1 = models.CharField(verbose_name="Address1*", max_length=250L, blank=True, null=True)
    address2 = models.CharField(max_length=250L, blank=True, null=True)
    address3 = models.CharField(max_length=250L, blank=True, null=True)
    county = models.ForeignKey( Boundary, verbose_name="County*")
    state = models.ForeignKey(Boundary, related_name='StaffProvince')
    email = models.EmailField(blank=True, null=True)
    primary_contact_no = models.CharField('Primary Contact No*', max_length=20)
    secondary_contact_no = models.CharField(max_length=20, blank=True, null=True)

class Salary(Common_Info):
    staff = models.ForeignKey(Staff, verbose_name="staff*")
    from_date = models.DateField('From*')
    to_date = models.DateField('To*')
    salary_per_annum = models.IntegerField('Salary*(Per Annum)')
    added_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.staff.personal_info.first_name

class Paid_Salary(Common_Info):
    staff = models.ForeignKey(Staff, verbose_name="staff*")
    from_date = models.DateField('From*')
    to_date = models.DateField('To*')
    amount_paid = models.IntegerField('Amount Paid*')
    added_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.staff.personal_info.first_name
