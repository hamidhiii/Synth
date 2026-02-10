from django.db import models

class BarcodeRule(models.Model):
    pass

class ProcurementRule(models.Model):
    group_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: procurement.group')
    sequence = models.IntegerField(default=0)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    location_src_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    route_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location.route')
    route_sequence = models.IntegerField(default=0)
    delay = models.IntegerField(default=0)
    partner_address_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    warehouse_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.warehouse')

class ProcurementGroup(models.Model):
    pass

class Product(models.Model):
    stock_quant_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    stock_move_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    orderpoint_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    nbr_reordering_rules = models.IntegerField(default=0)
    reordering_min_qty = models.FloatField(default=0.0)
    reordering_max_qty = models.FloatField(default=0.0)

class ProductTemplate(models.Model):
    responsible_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.users')
    type = models.CharField(max_length=50, blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    description_pickingout = models.TextField(blank=True, null=True)
    description_pickingin = models.TextField(blank=True, null=True)
    location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    warehouse_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.warehouse')
    nbr_reordering_rules = models.IntegerField(default=0)
    reordering_min_qty = models.FloatField(default=0.0)
    reordering_max_qty = models.FloatField(default=0.0)

class ProductCategory(models.Model):
    pass

class RemovalStrategy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)

class PutAwayStrategy(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

class FixedPutAwayStrategy(models.Model):
    putaway_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.putaway')
    category_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.category')
    fixed_location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    sequence = models.IntegerField(default=0)

class Company(models.Model):
    propagation_minimum_delta = models.IntegerField(default=0)

class Partner(models.Model):
    picking_warn = models.CharField(max_length=50, blank=True, null=True)
    picking_warn_msg = models.TextField(blank=True, null=True)

class Incoterms(models.Model):
    pass

class Inventory(models.Model):
    total_qty = models.FloatField(default=0.0)
    exhausted = models.BooleanField(default=False)

class InventoryLine(models.Model):
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')

class Location(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    complete_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    child_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    comment = models.TextField(blank=True, null=True)
    posx = models.IntegerField(default=0)
    posy = models.IntegerField(default=0)
    posz = models.IntegerField(default=0)
    parent_left = models.IntegerField(default=0)
    parent_right = models.IntegerField(default=0)
    scrap_location = models.BooleanField(default=False)
    return_location = models.BooleanField(default=False)
    removal_strategy_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.removal')
    putaway_strategy_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.putaway')
    barcode = models.CharField(max_length=255, blank=True, null=True)
    branch_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.branch')
    quant_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

class Route(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    sequence = models.IntegerField(default=0)
    product_selectable = models.BooleanField(default=False)
    product_categ_selectable = models.BooleanField(default=False)
    warehouse_selectable = models.BooleanField(default=False)
    supplied_wh_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.warehouse')
    supplier_wh_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.warehouse')
    product_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    categ_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    warehouse_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

class PushedFlow(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    route_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location.route')
    delay = models.IntegerField(default=0)
    propagate = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    warehouse_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.warehouse')
    route_sequence = models.IntegerField(default=0)
    sequence = models.IntegerField(default=0)

class StockMove(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)
    priority = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    ordered_qty = models.FloatField(default=0.0)
    product_uom = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.uom')
    picking_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking')
    picking_partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    note = models.TextField(blank=True, null=True)
    backorder_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking')
    origin = models.CharField(max_length=255, blank=True, null=True)
    scrapped = models.BooleanField(default=False)
    scrap_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    group_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: procurement.group')
    rule_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: procurement.rule')
    push_rule_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location.path')
    picking_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    inventory_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.inventory')
    move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    move_line_nosuggest_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    origin_returned_move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.move')
    returned_move_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    restrict_partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    route_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    warehouse_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.warehouse')
    has_tracking = models.CharField(max_length=50, blank=True, null=True)
    quantity_done = models.FloatField(default=0.0)
    show_operations = models.BooleanField(default=False)
    show_details_visible = models.BooleanField(default=False)
    show_reserved_availability = models.BooleanField(default=False)
    picking_code = models.CharField(max_length=50, blank=True, null=True)
    product_type = models.CharField(max_length=50, blank=True, null=True)
    additional = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    is_initial_demand_editable = models.BooleanField(default=False)
    is_quantity_done_editable = models.BooleanField(default=False)
    reference = models.CharField(max_length=255, blank=True, null=True)
    has_move_lines = models.BooleanField(default=False)
    out_qty = models.FloatField(default=0.0)
    bal_qty = models.FloatField(default=0.0)
    move_type = models.CharField(max_length=50, blank=True, null=True)

class StockMoveLine(models.Model):
    product_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.product')
    product_uom_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.uom')
    product_uom_qty = models.FloatField(default=0.0)
    ordered_qty = models.FloatField(default=0.0)
    qty_done = models.FloatField(default=0.0)
    package_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.quant.package')
    lot_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.production.lot')
    lot_name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    owner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    location_dest_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    from_loc = models.CharField(max_length=255, blank=True, null=True)
    to_loc = models.CharField(max_length=255, blank=True, null=True)
    lots_visible = models.BooleanField(default=False)
    state = models.CharField(max_length=50, blank=True, null=True)
    is_initial_demand_editable = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    consume_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    produce_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    reference = models.CharField(max_length=255, blank=True, null=True)
    in_entire_package = models.BooleanField(default=False)

class PickingType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    color = models.IntegerField(default=0)
    sequence = models.IntegerField(default=0)
    sequence_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: ir.sequence')
    code = models.CharField(max_length=50, blank=True, null=True)
    return_picking_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    show_entire_packs = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    last_done_picking = models.CharField(max_length=255, blank=True, null=True)
    count_picking_draft = models.IntegerField(default=0)
    count_picking_ready = models.IntegerField(default=0)
    count_picking = models.IntegerField(default=0)
    count_picking_waiting = models.IntegerField(default=0)
    count_picking_late = models.IntegerField(default=0)
    count_picking_backorders = models.IntegerField(default=0)
    rate_picking_late = models.IntegerField(default=0)
    rate_picking_backorders = models.IntegerField(default=0)

class Picking(models.Model):
    note = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    move_lines = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    printed = models.BooleanField(default=False)
    product_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.product')
    show_operations = models.BooleanField(default=False)
    show_lots_text = models.BooleanField(default=False)
    has_tracking = models.BooleanField(default=False)

class ProductionLot(models.Model):
    ref = models.CharField(max_length=255, blank=True, null=True)
    quant_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    create_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.FloatField(default=0.0)

class StockQuant(models.Model):
    in_date = models.DateTimeField(blank=True, null=True)

class QuantPackage(models.Model):
    quant_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    current_picking_move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    current_picking_id = models.BooleanField(default=False)
    current_source_location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    current_destination_location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    is_processed = models.BooleanField(default=False)

class StockScrap(models.Model):
    origin = models.CharField(max_length=255, blank=True, null=True)
    tracking = models.CharField(max_length=50, blank=True, null=True)
    owner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.move')
    picking_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking')
    scrap_qty = models.FloatField(default=0.0)
    date_expected = models.DateTimeField(blank=True, null=True)

class Warehouse(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    view_location_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    lot_stock_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    code = models.CharField(max_length=255, blank=True, null=True)
    wh_input_stock_loc_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    wh_qc_stock_loc_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    wh_output_stock_loc_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    wh_pack_stock_loc_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location')
    mto_pull_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: procurement.rule')
    pick_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    pack_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    out_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    in_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    int_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.picking.type')
    crossdock_route_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location.route')
    reception_route_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location.route')
    delivery_route_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: stock.location.route')
    branch_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.branch')

class Orderpoint(models.Model):
    pass

class PlannerInventory(models.Model):
    pass

