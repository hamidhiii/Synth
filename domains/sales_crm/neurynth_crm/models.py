from django.db import models

class CalendarEvent(models.Model):
    opportunity_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: crm.lead')

class Lead(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    date_action_last = models.DateTimeField(blank=True, null=True)
    email_from = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    team_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: crm.team')
    kanban_state = models.CharField(max_length=50, blank=True, null=True)
    email_cc = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    partner_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.users')
    referred = models.CharField(max_length=255, blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    day_open = models.FloatField(default=0.0)
    day_close = models.FloatField(default=0.0)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    date_conversion = models.DateTimeField(blank=True, null=True)
    message_bounce = models.IntegerField(default=0)
    probability = models.FloatField(default=0.0)
    planned_revenue = models.FloatField(default=0.0)
    date_deadline = models.DateField(blank=True, null=True)
    color = models.IntegerField(default=0)
    partner_address_name = models.CharField(max_length=255, blank=True, null=True)
    partner_address_email = models.CharField(max_length=255, blank=True, null=True)
    company_currency = models.TextField(blank=True, null=True, help_text='Odoo Many2one: Currency')
    user_email = models.CharField(max_length=255, blank=True, null=True)
    user_login = models.CharField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    street2 = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.country.state')
    country_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.country')
    phone = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    function = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner.title')
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    meeting_count = models.IntegerField(default=0)
    lost_reason = models.TextField(blank=True, null=True, help_text='Odoo Many2one: crm.lost.reason')

class Tag(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.IntegerField(default=0)

class LostReason(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)

class Stage(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)
    probability = models.FloatField(default=0.0)
    on_change = models.BooleanField(default=False)
    requirements = models.TextField(blank=True, null=True)

class Team(models.Model):
    use_leads = models.BooleanField(default=False)
    use_opportunities = models.BooleanField(default=False)
    alias_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mail.alias')
    dashboard_graph_model = models.CharField(max_length=50, blank=True, null=True)

class Partner(models.Model):
    team_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: crm.team')
    opportunity_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    meeting_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    opportunity_count = models.IntegerField(default=0)
    meeting_count = models.IntegerField(default=0)

class Users(models.Model):
    target_sales_won = models.IntegerField(default=0)
    target_sales_done = models.IntegerField(default=0)

class PlannerCrm(models.Model):
    pass

