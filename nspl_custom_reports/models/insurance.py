from odoo import models, fields

class Insurance(models.Model):
    _name = 'insurance.master'
    _description = 'Insurance Master'

    name = fields.Char(string="Insurance Name", required=True)