from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    hsn_code = fields.Char(string="HSN Code", related="product_id.l10n_in_hsn_code", store=True)
