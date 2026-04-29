from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    price_term_id = fields.Many2one('price.term',string="Price Term")
    insurance_id = fields.Many2one('insurance.master', string="Insurance")
    
    
    order_type = fields.Selection([
        ('normal', 'Normal'),
        ('export', 'Export'),
    ], string='Order Type', default='normal')


    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        invoice_vals['order_type'] = self.order_type
        invoice_vals['name'] = '/'
        return invoice_vals

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.quotation.custom') or '/'
        return super().create(vals_list)