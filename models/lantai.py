from odoo import fields, api, _
from . import bangunan


class BangunanLantai(bangunan.BangunanBangunan):
    _name = 'bangunan.lantai'
    _description = 'Bangunan Lantai Model'

    @api.multi
    def open_bangunan_ruang(self):
        return {
            'name': _('Ruang'),
            # 'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'bangunan.ruang',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_ruang_count(self):
        count = self.env['bangunan.ruang'].search_count([])
        self.ruang_count = count

    bangunan_id = fields.Many2one('bangunan.bangunan', string='Bangunan ID')
    ruang_count = fields.Integer(string='Ruang', compute='get_ruang_count')
