from django.db import models

class EmployeeCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.IntegerField(default=0)
    employee_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

class Job(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    employee_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    department_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.department')
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')

class Employee(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.users')
    active = models.BooleanField(default=False)
    birthday = models.DateField(blank=True, null=True)
    ssnid = models.CharField(max_length=255, blank=True, null=True)
    sinid = models.CharField(max_length=255, blank=True, null=True)
    identification_id = models.CharField(max_length=255, blank=True, null=True)
    passport_id = models.CharField(max_length=255, blank=True, null=True)
    permit_no = models.CharField(max_length=255, blank=True, null=True)
    visa_no = models.CharField(max_length=255, blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    work_phone = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    work_email = models.CharField(max_length=255, blank=True, null=True)
    work_location = models.CharField(max_length=255, blank=True, null=True)
    job_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.job')
    department_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.department')
    parent_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.employee')
    child_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    coach_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.employee')
    notes = models.TextField(blank=True, null=True)
    color = models.IntegerField(default=0)

class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    parent_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.department')
    child_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    manager_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: hr.employee')
    member_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    jobs_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    note = models.TextField(blank=True, null=True)
    color = models.IntegerField(default=0)

class Alias(models.Model):
    alias_contact = models.CharField(max_length=50, blank=True, null=True)

class Partner(models.Model):
    pass

class User(models.Model):
    employee_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

