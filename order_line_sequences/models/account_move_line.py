from odoo import fields, models,api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    sequence_no = fields.Integer("#", compute='_compute_sequence_number',)

    @api.depends('sequence', 'move_id')
    def _compute_sequence_number(self):
        for move in self.mapped('move_id'):
            sequence_number = 1
            for line in move.invoice_line_ids:
                if line.display_type:
                    line.sequence_no = sequence_number
                    sequence_number += 0
                else:
                    line.sequence_no = sequence_number
                    sequence_number += 1
