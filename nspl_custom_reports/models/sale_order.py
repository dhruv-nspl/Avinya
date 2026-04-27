from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    price_term_id = fields.Many2one('price.term',string="Price Term")
    insurance_id = fields.Many2one('insurance.master', string="Insurance")