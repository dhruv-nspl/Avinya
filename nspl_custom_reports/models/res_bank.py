from odoo import models, fields

class ResBank(models.Model):
    _inherit = "res.bank"
    
    bank_ad_code = fields.Char("Bank AD Code")
    bank_ifsc_code = fields.Char("Bank IFSC Code")

