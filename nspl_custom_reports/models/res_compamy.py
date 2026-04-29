from odoo import models,fields

class ResCompany(models.Model):
    _inherit = "res.company"
    
    iec_no = fields.Char(string="IEC No")
    lut_no = fields.Char(string="LUT No")