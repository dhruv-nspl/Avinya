# -*- coding: utf-8 -*-
from odoo import models, fields


class ResCompany(models.Model):
    _inherit = "res.company"

    invoice_signatory = fields.Many2one("res.users")
    invoice_sign = fields.Binary(string="Invoice Signature", copy=False)
