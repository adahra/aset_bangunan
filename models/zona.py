from odoo import fields
from . import area


class BangunanZona(area.BangunanArea):
    _name = 'bangunan.zona'
    _description = 'Bangunan Zona Model'

    # name = fields.Char(string='Bangunan Zona Nama', required=True)
    # kode = fields.Char(string='Bangunan Zona Kode')
    area_id = fields.Many2one('bangunan.area', string='Bangunan Area ID')
