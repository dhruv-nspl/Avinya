from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"


    def _l10n_in_get_hsn_summary_table(self):
        self.ensure_one()
        base_lines, _tax_lines = self._get_rounded_base_and_tax_lines()
        display_uom = self.env.user.has_group('uom.group_uom')
        return self.env['account.tax']._l10n_in_get_hsn_summary_table(base_lines, display_uom)

    def _get_rounded_base_and_tax_lines(self):
        self.ensure_one()
        AccountTax = self.env['account.tax']

        base_lines = []
        for line in self.order_line.filtered(lambda l: not l.display_type):
            base_line = self._prepare_product_base_line_for_taxes_computation(line)
            base_lines.append(base_line)

        AccountTax._add_tax_details_in_base_lines(base_lines, self.company_id)
        AccountTax._round_base_lines_tax_details(base_lines, self.company_id)

        return base_lines, []

    def _prepare_product_base_line_for_taxes_computation(self, line):
        self.ensure_one()
        price_unit = line.price_unit * (1 - (line.discount or 0.0) / 100.0)

        return self.env['account.tax']._prepare_base_line_for_taxes_computation(
            line,
            tax_ids=line.tax_ids,
            currency_id=self.currency_id,
            product_id=line.product_id,
            account_id=line.product_id.product_tmpl_id._get_product_accounts().get('expense'),
            analytic_distribution=line.analytic_distribution if hasattr(line, 'analytic_distribution') else {},
            price_unit=price_unit,
            quantity=line.product_qty,
            discount=line.discount or 0.0,
            sign=1,
            uom_id=line.product_uom_id,
            l10n_in_hsn_code=line.product_id.l10n_in_hsn_code if hasattr(line.product_id, 'l10n_in_hsn_code') else False,
        )
        
        
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('purchase.order.custom') or '/'
        return super().create(vals_list)