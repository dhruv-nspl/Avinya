from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    price_term_id = fields.Many2one('price.term',string="Price Term")
    insurance_id = fields.Many2one('insurance.master', string="Insurance")
    kind_attenstion_ids = fields.Many2many('res.partner', string="Kind Attn.")

    order_type = fields.Selection([
        ('normal', 'Normal'),
        ('export', 'Export'),
    ], string='Order Type', default='normal')

    def _get_financial_year(self, inv_date):
           if not inv_date:
               inv_date = fields.Date.today()
    
           year = inv_date.year
    
           if inv_date.month >= 4:
               start = year
               end = year + 1
           else:
               start = year - 1
               end = year
    
           return f"{str(start)[-2:]}-{str(end)[-2:]}"

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        fy = self._get_financial_year(self.date_order)
        if self.order_type == 'export':
            seq = self.env['ir.sequence'].next_by_code('invoice.export.custom') or '/'
            name = f"{seq}/{fy}"
        else:
            seq = self.env['ir.sequence'].next_by_code('invoice.normal.custom') or '/'
            name = f"{seq}/{fy}"
        invoice_vals['inv_type'] = self.order_type
        invoice_vals['name'] = name
        return invoice_vals

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == '/':
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.quotation.custom') or '/'
        return super().create(vals_list)

   

    @api.onchange('order_type')
    def _onchange_order_type(self):
        if self.order_type == 'export':
            for line in self.order_line:
                line.tax_ids = False
                
    @api.onchange('partner_id')
    def _onchange_partner_id_kind_attention(self):
        for rec in self:
            rec.kind_attenstion_ids = False