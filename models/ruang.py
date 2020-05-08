from odoo import fields
from . import lantai


class BangunanRuang(lantai.BangunanLantai):
    _name = 'bangunan.ruang'
    _description = 'Bangunan Ruang Model'

    lantai_id = fields.Many2one('bangunan.lantai', string='Bangunan Lantai ID')
