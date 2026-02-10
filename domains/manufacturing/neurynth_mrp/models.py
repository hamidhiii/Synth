from django.db import models

class MrpBom(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    bom_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    sequence = models.IntegerField(default=0)

class MrpBomLine(models.Model):
    has_attachments = models.BooleanField(default=False)

class MrpDocument(models.Model):
    ir_attachment_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: ir.attachment')
    active = models.BooleanField(default=False)

class MrpProductionMessage(models.Model):
    name = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    product_tmpl_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.template')
    product_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.product')
    bom_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.bom')
    workcenter_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.workcenter')
    valid_until = models.DateField(blank=True, null=True)
    routing_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.routing')

class MrpProduction(models.Model):
    product_tmpl_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.template')
    date_start = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    workorder_count = models.IntegerField(default=0)
    workorder_done_count = models.IntegerField(default=0)
    user_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.users')
    qty_produced = models.FloatField(default=0.0)
    has_moves = models.BooleanField(default=False)
    scrap_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    scrap_count = models.IntegerField(default=0)
    priority = models.CharField(max_length=50, blank=True, null=True)
    is_locked = models.BooleanField(default=False)
    show_final_lots = models.BooleanField(default=False)
    production_location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')

class MrpRouting(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)

class MrpRoutingWorkcenter(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    workcenter_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.workcenter')
    note = models.TextField(blank=True, null=True)
    worksheet = models.BinaryField(blank=True, null=True)
    time_mode_batch = models.IntegerField(default=0)
    time_cycle = models.FloatField(default=0.0)
    workorder_count = models.IntegerField(default=0)
    batch_size = models.FloatField(default=0.0)
    workorder_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

class MrpUnbuild(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    has_tracking = models.CharField(max_length=50, blank=True, null=True)

class MrpWorkcenter(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    time_efficiency = models.FloatField(default=0.0)
    active = models.BooleanField(default=False)
    code = models.CharField(max_length=255, blank=True, null=True)
    color = models.IntegerField(default=0)
    time_start = models.FloatField(default=0.0)
    time_stop = models.FloatField(default=0.0)
    routing_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    order_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    workorder_count = models.IntegerField(default=0)
    workorder_ready_count = models.IntegerField(default=0)
    workorder_progress_count = models.IntegerField(default=0)
    workorder_pending_count = models.IntegerField(default=0)
    workorder_late_count = models.IntegerField(default=0)
    time_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    oee = models.FloatField(default=0.0)
    oee_target = models.FloatField(default=0.0)
    performance = models.IntegerField(default=0)
    workcenter_load = models.FloatField(default=0.0)

class MrpWorkcenterProductivityLoss(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)
    manual = models.BooleanField(default=False)

class MrpWorkcenterProductivity(models.Model):
    workcenter_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.workcenter')
    workorder_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.workorder')
    description = models.TextField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(default=0.0)

class MrpWorkorder(models.Model):
    qty_production = models.FloatField(default=0.0)
    qty_remaining = models.FloatField(default=0.0)
    tracking = models.CharField(max_length=50, blank=True, null=True)
    production_messages = models.TextField(blank=True, null=True)
    next_work_order_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.workorder')
    scrap_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    scrap_count = models.IntegerField(default=0)
    production_date = models.DateTimeField(blank=True, null=True)
    color = models.IntegerField(default=0)

class ProcurementRule(models.Model):
    action = models.CharField(max_length=50, blank=True, null=True)

class ProductTemplate(models.Model):
    bom_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    bom_count = models.IntegerField(default=0)
    used_in_bom_count = models.IntegerField(default=0)
    mo_count = models.IntegerField(default=0)

class ProductProduct(models.Model):
    bom_count = models.IntegerField(default=0)
    used_in_bom_count = models.IntegerField(default=0)
    mo_count = models.IntegerField(default=0)

class Company(models.Model):
    pass

class StockMoveLine(models.Model):
    workorder_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.workorder')
    production_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.production')
    lot_produced_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.production.lot')
    done_wo = models.BooleanField(default=False)
    done_move = models.BooleanField(default=False)

class StockMove(models.Model):
    created_production_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.production')
    active_move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    bom_line_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: mrp.bom.line')
    unit_factor = models.FloatField(default=0.0)
    needs_lots = models.BooleanField(default=False)
    order_finished_lot_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    finished_lots_exist = models.BooleanField(default=False)

class PushedFlow(models.Model):
    pass

class StockPickingType(models.Model):
    code = models.CharField(max_length=50, blank=True, null=True)

class StockProductionLot(models.Model):
    pass

class StockScrap(models.Model):
    pass

class StockWarehouse(models.Model):
    pass

