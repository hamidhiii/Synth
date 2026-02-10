from django.db import models

class AccountInvoice(models.Model):
    team_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: crm.team')
    comment = models.TextField(blank=True, null=True)

class AccountInvoiceLine(models.Model):
    layout_category_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: sale.layout_category')
    layout_category_sequence = models.IntegerField(default=0)
    price_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

class AccountAnalyticLine(models.Model):
    so_line = models.TextField(blank=True, null=True, help_text='Odoo Many2one: sale.order.line')

class IrModelFields(models.Model):
    pass

class ProductPricelist(models.Model):
    pass

class ProductProduct(models.Model):
    sales_count = models.IntegerField(default=0)

class ProductTemplate(models.Model):
    service_type = models.CharField(max_length=50, blank=True, null=True)
    sale_line_warn = models.CharField(max_length=50, blank=True, null=True)
    sale_line_warn_msg = models.TextField(blank=True, null=True)
    sales_count = models.IntegerField(default=0)

class ResCompany(models.Model):
    sale_note = models.TextField(blank=True, null=True)

class ResPartner(models.Model):
    sale_order_count = models.IntegerField(default=0)
    sale_order_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    sale_warn = models.CharField(max_length=50, blank=True, null=True)
    sale_warn_msg = models.TextField(blank=True, null=True)

class SaleOrder(models.Model):
    pass

class SaleOrderLine(models.Model):
    order_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: sale.order')
    name = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(default=0)
    invoice_lines = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    price_unit = models.FloatField(default=0.0)
    price_subtotal = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    price_tax = models.FloatField(default=0.0)
    price_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    price_reduce = models.FloatField(default=0.0)
    tax_id = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    price_reduce_taxinc = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    price_reduce_taxexcl = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    discount = models.FloatField(default=0.0)
    product_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.product')
    product_updatable = models.BooleanField(default=False)
    product_uom_qty = models.FloatField(default=0.0)
    product_uom = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.uom')
    product_image = models.BinaryField(blank=True, null=True)
    qty_delivered_updateable = models.BooleanField(default=False)
    qty_delivered = models.FloatField(default=0.0)
    salesman_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: order_id.user_id')
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: order_id.currency_id')
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: order_id.company_id')
    order_partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: order_id.partner_id')
    analytic_tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    amt_to_invoice = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    amt_invoiced = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    layout_category_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: sale.layout_category')
    layout_category_sequence = models.IntegerField(default=0)

class CrmTeam(models.Model):
    use_invoices = models.BooleanField(default=False)

class SaleLayoutCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)
    subtotal = models.BooleanField(default=False)
    pagebreak = models.BooleanField(default=False)

