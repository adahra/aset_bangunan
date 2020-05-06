from odoo import fields
from . import lantai


class BangunanRuang(lantai.BangunanLantai):
    _name = 'bangunan.ruang'
    _description = 'Bangunan Ruang Model'

    # bangunan_id = fields.Many2one('bangunan.bangunan', string='Bangunan ID')
    lantai_id = fields.Many2one('bangunan.lantai', string='Bangunan Lantai ID')
