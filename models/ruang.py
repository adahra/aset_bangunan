from odoo import fields, models


class BangunanRuang(models.Model):
    _name = 'bangunan.ruang'
    _description = 'Bangunan Ruang Model'

    name = fields.Char(string='Bangunan Ruang Nama', required=True)
    kode = fields.Char(string='Bangunan Ruang Kode')
    bangunan_id = fields.Many2one('bangunan.bangunan', string='Bangunan ID')
    lantai_id = fields.Many2one('bangunan.lantai', string='Bangunan Lantai ID')
