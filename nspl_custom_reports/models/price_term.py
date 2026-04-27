from odoo import models,fields

class PriceTerm(models.Model):
    _name = 'price.term'
    
    name = fields.Char(string="Price Term")