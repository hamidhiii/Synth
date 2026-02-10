from django.db import models

class AccountAccountType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    include_initial_balance = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

class AccountAccountTag(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    applicability = models.CharField(max_length=50, blank=True, null=True)
    color = models.IntegerField(default=0)
    active = models.BooleanField(default=False)

class AccountAccount(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    deprecated = models.BooleanField(default=False)
    internal_type = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    group_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.group')
    opening_debit = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    opening_credit = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

class AccountGroup(models.Model):
    parent_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.group')
    parent_left = models.IntegerField(default=0)
    parent_right = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    code_prefix = models.CharField(max_length=255, blank=True, null=True)

class AccountJournal(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    type_control_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    sequence = models.IntegerField(default=0)
    groups_id = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    refund_sequence = models.BooleanField(default=False)
    at_least_one_inbound = models.BooleanField(default=False)
    at_least_one_outbound = models.BooleanField(default=False)
    profit_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    loss_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    belongs_to_company = models.BooleanField(default=False)
    bank_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner.bank')
    bank_statements_source = models.CharField(max_length=50, blank=True, null=True)
    bank_acc_number = models.CharField(max_length=255, blank=True, null=True)
    bank_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.bank')

class ResPartnerBank(models.Model):
    journal_id = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

class AccountTaxGroup(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)

class AccountTax(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    type_tax_use = models.CharField(max_length=50, blank=True, null=True)
    tax_adjustment = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    children_tax_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    amount = models.FloatField(default=0.0)
    account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    refund_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    description = models.CharField(max_length=255, blank=True, null=True)
    analytic = models.BooleanField(default=False)
    tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_group_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax.group')
    hide_tax_exigibility = models.BooleanField(default=False)

class AccountReconcileModel(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)
    has_second_line = models.BooleanField(default=False)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    label = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(default=0.0)
    tax_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax')
    analytic_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.analytic.account')
    second_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    second_journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    second_label = models.CharField(max_length=255, blank=True, null=True)
    second_amount = models.FloatField(default=0.0)
    second_tax_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax')
    second_analytic_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.analytic.account')

class AccountAnalyticLine(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    product_uom_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.uom')
    product_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.product')
    move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.move.line')
    code = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    amount_currency = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    analytic_amount_currency = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')

class AccountCashboxLine(models.Model):
    coin_value = models.FloatField(default=0.0)
    number = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0.0)
    cashbox_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.bank.statement.cashbox')

class AccountBankStmtCashWizard(models.Model):
    cashbox_lines_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')

class AccountBankStatement(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    balance_end_real = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    state = models.CharField(max_length=50, blank=True, null=True)
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    journal_type = models.CharField(max_length=50, blank=True, null=True)
    total_entry_encoding = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    balance_end = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    difference = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    move_line_count = models.IntegerField(default=0)
    all_lines_reconciled = models.BooleanField(default=False)
    user_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.users')
    cashbox_start_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.bank.statement.cashbox')
    cashbox_end_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.bank.statement.cashbox')
    is_difference_zero = models.BooleanField(default=False)

class AccountBankStatementLine(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    bank_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner.bank')
    account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    statement_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.bank.statement')
    journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    ref = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    sequence = models.IntegerField(default=0)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    journal_entry_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    amount_currency = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    state = models.CharField(max_length=50, blank=True, null=True)

class AccountCashRounding(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    strategy = models.CharField(max_length=50, blank=True, null=True)
    account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')

class AccountInvoice(models.Model):
    refund_invoice_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.invoice')
    number = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    refund_invoice_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    company_currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    payment_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    payment_move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    outstanding_credits_debits_widget = models.TextField(blank=True, null=True)
    payments_widget = models.TextField(blank=True, null=True)
    has_outstanding = models.BooleanField(default=False)
    sequence_number_next = models.CharField(max_length=255, blank=True, null=True)
    sequence_number_next_prefix = models.CharField(max_length=255, blank=True, null=True)

class AccountInvoiceLine(models.Model):
    name = models.TextField(blank=True, null=True)
    product_image = models.BinaryField(blank=True, null=True)
    price_unit = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    analytic_tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    company_currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    is_rounding_line = models.BooleanField(default=False)

class AccountInvoiceTax(models.Model):
    invoice_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.invoice')
    name = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax')
    account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    account_analytic_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.analytic.account')
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    amount_rounding = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    amount_total = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    manual = models.BooleanField(default=False)
    sequence = models.IntegerField(default=0)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    base = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)

class AccountPaymentTerm(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    sequence = models.IntegerField(default=0)

class AccountPaymentTermLine(models.Model):
    value_amount = models.FloatField(default=0.0)
    days = models.IntegerField(default=0)
    payment_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.payment.term')
    sequence = models.IntegerField(default=0)

class account_journal(models.Model):
    kanban_dashboard = models.TextField(blank=True, null=True)
    kanban_dashboard_graph = models.TextField(blank=True, null=True)
    show_on_dashboard = models.BooleanField(default=False)
    color = models.IntegerField(default=0)
    account_setup_bank_data_done = models.BooleanField(default=False)

class AccountMove(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    state = models.CharField(max_length=50, blank=True, null=True)
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    narration = models.TextField(blank=True, null=True)
    matched_percentage = models.FloatField(default=0.0)
    dummy_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')

class AccountMoveLine(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.FloatField(default=0.0)
    product_uom_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.uom')
    product_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: product.product')
    debit = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    credit = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    debit_cash_basis = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    credit_cash_basis = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    amount_currency = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    tax_base_amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    narration = models.TextField(blank=True, null=True)
    ref = models.CharField(max_length=255, blank=True, null=True)
    payment_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.payment')
    statement_line_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.bank.statement.line')
    reconciled = models.BooleanField(default=False)
    full_reconcile_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.full.reconcile')
    date = models.DateField(blank=True, null=True)
    analytic_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_line_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax')
    analytic_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.analytic.account')
    analytic_tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    counterpart = models.CharField(max_length=255, blank=True, null=True)
    invoice_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.invoice')
    partner_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.partner')
    user_type_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.type')
    parent_state = models.CharField(max_length=255, blank=True, null=True)
    is_unaffected_earnings_line = models.BooleanField(default=False)

class AccountPartialReconcile(models.Model):
    debit_move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.move.line')
    credit_move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.move.line')
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    amount_currency = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    full_reconcile_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.full.reconcile')

class AccountFullReconcile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    partial_reconcile_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    reconciled_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    exchange_move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.move')

class account_payment_method(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)

class account_payment(models.Model):
    company_id = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.CharField(max_length=50, blank=True, null=True)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)
    destination_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    destination_journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    invoice_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    has_invoices = models.BooleanField(default=False)
    payment_difference = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    payment_difference_handling = models.CharField(max_length=50, blank=True, null=True)
    writeoff_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    move_line_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    move_reconciled = models.BooleanField(default=False)

class AccountAccountTemplate(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    code = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    tax_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    group_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.group')

class AccountChartTemplate(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    parent_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.chart.template')
    code_digits = models.IntegerField(default=0)
    currency_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.currency')
    use_anglo_saxon = models.BooleanField(default=False)
    account_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    bank_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    property_account_receivable_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_account_payable_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_account_expense_categ_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_account_income_categ_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_account_expense_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_account_income_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_stock_account_input_categ_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_stock_account_output_categ_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    property_stock_valuation_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')

class AccountTaxTemplate(models.Model):
    chart_template_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.chart.template')
    name = models.CharField(max_length=255, blank=True, null=True)
    type_tax_use = models.CharField(max_length=50, blank=True, null=True)
    tax_adjustment = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    children_tax_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    amount = models.FloatField(default=0.0)
    description = models.CharField(max_length=255, blank=True, null=True)
    analytic = models.BooleanField(default=False)
    tag_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_group_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax.group')

class AccountFiscalPositionTemplate(models.Model):
    sequence = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    chart_template_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.chart.template')
    account_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(default=False)
    vat_required = models.BooleanField(default=False)
    state_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    zip_from = models.IntegerField(default=0)
    zip_to = models.IntegerField(default=0)

class AccountFiscalPositionTaxTemplate(models.Model):
    position_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.fiscal.position.template')
    tax_src_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax.template')
    tax_dest_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax.template')

class AccountFiscalPositionAccountTemplate(models.Model):
    position_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.fiscal.position.template')
    account_src_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    account_dest_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')

class AccountReconcileModelTemplate(models.Model):
    chart_template_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.chart.template')
    name = models.CharField(max_length=255, blank=True, null=True)
    sequence = models.IntegerField(default=0)
    has_second_line = models.BooleanField(default=False)
    account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    label = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(default=0.0)
    tax_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax.template')
    second_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account.template')
    second_label = models.CharField(max_length=255, blank=True, null=True)
    second_amount = models.FloatField(default=0.0)
    second_tax_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax.template')

class ResCompany(models.Model):
    fiscalyear_last_day = models.IntegerField(default=0)
    fiscalyear_last_month = models.CharField(max_length=50, blank=True, null=True)
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    expects_chart_of_accounts = models.BooleanField(default=False)
    chart_template_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.chart.template')
    bank_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=255, blank=True, null=True)
    accounts_code_digits = models.IntegerField(default=0)
    tax_cash_basis_journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    currency_exchange_journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.journal')
    anglo_saxon_accounting = models.BooleanField(default=False)
    property_stock_account_input_categ_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    property_stock_account_output_categ_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    property_stock_valuation_account_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.account')
    bank_journal_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_exigibility = models.BooleanField(default=False)
    account_opening_move_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: Opening Journal Entry')
    account_opening_journal_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: Opening Journal')
    account_opening_date = models.DateField(blank=True, null=True)
    account_setup_company_data_done = models.BooleanField(default=False)
    account_setup_bank_data_done = models.BooleanField(default=False)
    account_setup_fy_data_done = models.BooleanField(default=False)
    account_setup_coa_done = models.BooleanField(default=False)
    account_setup_bar_closed = models.BooleanField(default=False)

class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: res.company')
    account_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    tax_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    note = models.TextField(blank=True, null=True)
    auto_apply = models.BooleanField(default=False)
    vat_required = models.BooleanField(default=False)
    state_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    zip_from = models.IntegerField(default=0)
    zip_to = models.IntegerField(default=0)
    states_count = models.IntegerField(default=0)

class AccountFiscalPositionTax(models.Model):
    tax_src_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax')
    tax_dest_id = models.TextField(blank=True, null=True, help_text='Odoo Many2one: account.tax')

class AccountFiscalPositionAccount(models.Model):
    pass

class ResPartner(models.Model):
    debit_limit = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    contracts_count = models.IntegerField(default=0)
    journal_item_count = models.IntegerField(default=0)
    invoice_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    contract_ids = models.TextField(blank=True, null=True, help_text='Odoo relationship field')
    bank_account_count = models.IntegerField(default=0)
    trust = models.CharField(max_length=50, blank=True, null=True)
    invoice_warn = models.CharField(max_length=50, blank=True, null=True)
    invoice_warn_msg = models.TextField(blank=True, null=True)

class ProductCategory(models.Model):
    pass

class ProductTemplate(models.Model):
    pass

class ProductProduct(models.Model):
    pass

class PlannerAccount(models.Model):
    pass

