from django import forms
from hrmanagement.models import *

from farmer.models import *
from django.contrib.auth.models import User



GENDER_CHOICES = (('male', 'male'), ('female', 'female'), ('other', 'other'))

class add_staff_form(forms.Form):

    position_type_list = Position_Type.objects.filter(active=2)
    salutation_list = Salutations.objects.filter(active=2)
    maritial_status_list = Maritial_Status.objects.filter(active=2)
    users_list = User.objects.all()

    prefix = forms.ModelChoiceField(queryset=salutation_list, label="Prefix*")
    first_name = forms.CharField(max_length=60, label="First name*")
    middle_name =  forms.CharField(max_length=60, required=False)
    Last_name = forms.CharField(max_length=60, required=False)
    farmer_id =forms.CharField(max_length=100, label="Staff ID*(Republic ID or Voter ID)")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, label="Gender*")
    dob = forms.DateField(required= False, label="Date Of Birth")
    maritial_status = forms.ModelChoiceField(queryset=maritial_status_list, label="Marital Status*")

    staff_type_list = Staff_Type.objects.filter(active=2)
    person_list = Person.objects.all()
    skills_list = Skills.objects.filter(active=2)
    department_list = Department.objects.filter(active=2)
    designation_list = Designation.objects.filter(active=2)
    qualification = Educational_Qualification.objects.filter(active=2)

    staff_type = forms.ModelChoiceField(queryset=staff_type_list, label="Staff Type*")

    skills = forms.ModelMultipleChoiceField(queryset=Skills.objects.all(), required=False)
    department = forms.ModelChoiceField(queryset=department_list, required= False)
    designation = forms.ModelChoiceField(queryset=designation_list, required= False)
    qualification = forms.ModelMultipleChoiceField(queryset=Educational_Qualification.objects.all(), required=False)
    date_of_joining = forms.DateField(label="Joining Date*")
    date_of_leaving = forms.DateField(required= False, label="Leaving Date")
    photo = ImageWithThumbsField(upload_to='static/%Y/%m/%d', sizes=((90, 120), ((120, 118)), (180, 240), (360, 480)), blank=True, null=True)
    work_experience = forms.DecimalField(decimal_places=6, max_digits=10, label="Work Experience*(In Years)")



class add_salary_form(forms.ModelForm):

    staff_list1 = Salary.objects.all()
    salary_staff_list = [i.staff.id for i in staff_list1]
    staff_list2 = Staff.objects.exclude(id__in=salary_staff_list)
    staff = forms.ModelChoiceField(queryset=staff_list2, label="Staff*")
    class Meta:
        model = Salary
        exclude = ('created_on', 'added_by')



def cus_pay_salary_form(staff_id):

    class pay_salary_form(forms.ModelForm):

        class Meta:
            model = Paid_Salary
            fields = ('from_date', 'to_date', 'amount_paid')

        def clean(self):
            ''' validate payment'''
            cleaned_data = super(pay_salary_form, self).clean()
            from_date = cleaned_data.get('from_date')
            to_date = cleaned_data.get('to_date')
            amount_paid = cleaned_data.get('amount_paid')
            staff_obj = Staff.objects.get(id=staff_id)
            salary_obj = Salary.objects.get(staff__id= staff_id)
            if to_date and to_date:
                if from_date <= to_date:
                    if from_date >= salary_obj.from_date and from_date < salary_obj.to_date:
                        if to_date > salary_obj.from_date and to_date < salary_obj.to_date:
                            pass
                        else:
                            raise forms.ValidationError('To date should be between ' + str(salary_obj.from_date) + ' and ' + str(salary_obj.to_date))
                    else:
                        raise forms.ValidationError('From date should be between ' + str(salary_obj.from_date) + ' and ' + str(salary_obj.to_date))
                else:
                    raise forms.ValidationError('From date should  be less than to date')
            if amount_paid <= 0:
                raise forms.ValidationError('Amount should be greater than zero')
            payment_list = Paid_Salary.objects.filter(staff = staff_obj)
            total_amount_paid = 0
            for i in payment_list:
                total_amount_paid = total_amount_paid + i.amount_paid
            total = int(amount_paid) + total_amount_paid
            if total > salary_obj.salary_per_annum:
                raise forms.ValidationError('Amount is exceeding total configured payment for this staff')

            return cleaned_data   # clean method should always return cleaned data
    return pay_salary_form




class add_person_form(forms.ModelForm):

    class Meta:
        model = Person
        exclude = ('created_on')

from hrmanagement.models import Staff
def add_staff_address_form(staff_id):

    class cus_staff_address_form(forms.ModelForm):

        staff_obj = Staff.objects.filter(id =  staff_id)
        state_list = Boundary.objects.filter(parent=None)
        #staff = forms.ModelChoiceField(queryset = staff_obj, initial={'staff': staff_obj})
        state = forms.ModelChoiceField(queryset = state_list, label="State*")
        #county = forms.ModelChoiceField(queryset=[])
        class Meta:
            model = Staff_Address
            fields = ('state', 'county', 'address1', 'address2', 'address3', 'email', 'primary_contact_no', 'secondary_contact_no')


    return cus_staff_address_form
