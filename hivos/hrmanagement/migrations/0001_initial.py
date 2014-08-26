# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table(u'hrmanagement_department', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'hrmanagement', ['Department'])

        # Adding model 'Designation'
        db.create_table(u'hrmanagement_designation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'hrmanagement', ['Designation'])

        # Adding model 'Skill_Type'
        db.create_table(u'hrmanagement_skill_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'hrmanagement', ['Skill_Type'])

        # Adding model 'Skills'
        db.create_table(u'hrmanagement_skills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('skill_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hrmanagement.Skill_Type'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'hrmanagement', ['Skills'])

        # Adding model 'Staff_Type'
        db.create_table(u'hrmanagement_staff_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('active', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'hrmanagement', ['Staff_Type'])

        # Adding model 'Staff'
        db.create_table(u'hrmanagement_staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('staff_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hrmanagement.Staff_Type'])),
            ('personal_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['farmer.Person'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hrmanagement.Department'], null=True, blank=True)),
            ('date_of_joining', self.gf('django.db.models.fields.DateField')()),
            ('date_of_leaving', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('photo', self.gf('farmer.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('work_experience', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('active', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal(u'hrmanagement', ['Staff'])

        # Adding M2M table for field skills on 'Staff'
        m2m_table_name = db.shorten_name(u'hrmanagement_staff_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staff', models.ForeignKey(orm[u'hrmanagement.staff'], null=False)),
            ('skills', models.ForeignKey(orm[u'hrmanagement.skills'], null=False))
        ))
        db.create_unique(m2m_table_name, ['staff_id', 'skills_id'])

        # Adding M2M table for field qualification on 'Staff'
        m2m_table_name = db.shorten_name(u'hrmanagement_staff_qualification')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staff', models.ForeignKey(orm[u'hrmanagement.staff'], null=False)),
            ('educational_qualification', models.ForeignKey(orm[u'farmer.educational_qualification'], null=False))
        ))
        db.create_unique(m2m_table_name, ['staff_id', 'educational_qualification_id'])

        # Adding model 'Staff_Address'
        db.create_table(u'hrmanagement_staff_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hrmanagement.Staff'])),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=250L, null=True, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=250L, null=True, blank=True)),
            ('address3', self.gf('django.db.models.fields.CharField')(max_length=250L, null=True, blank=True)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['farmer.Boundary'])),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='StaffProvince', to=orm['farmer.Boundary'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('primary_contact_no', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('secondary_contact_no', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'hrmanagement', ['Staff_Address'])

        # Adding model 'Salary'
        db.create_table(u'hrmanagement_salary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hrmanagement.Staff'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
            ('salary_per_month', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hrmanagement', ['Salary'])

        # Adding model 'Paid_Salary'
        db.create_table(u'hrmanagement_paid_salary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 6, 0, 0))),
            ('modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hrmanagement.Staff'])),
            ('from_date', self.gf('django.db.models.fields.DateField')()),
            ('to_date', self.gf('django.db.models.fields.DateField')()),
            ('amount_paid', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'hrmanagement', ['Paid_Salary'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table(u'hrmanagement_department')

        # Deleting model 'Designation'
        db.delete_table(u'hrmanagement_designation')

        # Deleting model 'Skill_Type'
        db.delete_table(u'hrmanagement_skill_type')

        # Deleting model 'Skills'
        db.delete_table(u'hrmanagement_skills')

        # Deleting model 'Staff_Type'
        db.delete_table(u'hrmanagement_staff_type')

        # Deleting model 'Staff'
        db.delete_table(u'hrmanagement_staff')

        # Removing M2M table for field skills on 'Staff'
        db.delete_table(db.shorten_name(u'hrmanagement_staff_skills'))

        # Removing M2M table for field qualification on 'Staff'
        db.delete_table(db.shorten_name(u'hrmanagement_staff_qualification'))

        # Deleting model 'Staff_Address'
        db.delete_table(u'hrmanagement_staff_address')

        # Deleting model 'Salary'
        db.delete_table(u'hrmanagement_salary')

        # Deleting model 'Paid_Salary'
        db.delete_table(u'hrmanagement_paid_salary')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmer.boundary': {
            'Meta': {'object_name': 'Boundary'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'boundary_id': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmer.Boundary']", 'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'farmer.educational_qualification': {
            'Meta': {'object_name': 'Educational_Qualification'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmer.maritial_status': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Maritial_Status'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmer.person': {
            'Last_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Person'},
            'added_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'farmer_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maritial_status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmer.Maritial_Status']"}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'position_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmer.Position_Type']"}),
            'prefix': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmer.Salutations']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmer.position_type': {
            'Meta': {'object_name': 'Position_Type'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmer.salutations': {
            'Meta': {'unique_together': "(('name',),)", 'object_name': 'Salutations'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hrmanagement.department': {
            'Meta': {'object_name': 'Department'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hrmanagement.designation': {
            'Meta': {'object_name': 'Designation'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hrmanagement.paid_salary': {
            'Meta': {'object_name': 'Paid_Salary'},
            'amount_paid': ('django.db.models.fields.IntegerField', [], {}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hrmanagement.Staff']"}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        u'hrmanagement.salary': {
            'Meta': {'object_name': 'Salary'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'salary_per_month': ('django.db.models.fields.IntegerField', [], {}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hrmanagement.Staff']"}),
            'to_date': ('django.db.models.fields.DateField', [], {})
        },
        u'hrmanagement.skill_type': {
            'Meta': {'object_name': 'Skill_Type'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hrmanagement.skills': {
            'Meta': {'object_name': 'Skills'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'skill_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hrmanagement.Skill_Type']"})
        },
        u'hrmanagement.staff': {
            'Meta': {'object_name': 'Staff'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'date_of_joining': ('django.db.models.fields.DateField', [], {}),
            'date_of_leaving': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hrmanagement.Department']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'personal_info': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmer.Person']"}),
            'photo': ('farmer.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['farmer.Educational_Qualification']", 'null': 'True', 'blank': 'True'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['hrmanagement.Skills']", 'null': 'True', 'blank': 'True'}),
            'staff_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hrmanagement.Staff_Type']"}),
            'work_experience': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'})
        },
        u'hrmanagement.staff_address': {
            'Meta': {'object_name': 'Staff_Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'null': 'True', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '250L', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmer.Boundary']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'primary_contact_no': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'secondary_contact_no': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['hrmanagement.Staff']"}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'StaffProvince'", 'to': u"orm['farmer.Boundary']"})
        },
        u'hrmanagement.staff_type': {
            'Meta': {'object_name': 'Staff_Type'},
            'active': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 6, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hrmanagement']