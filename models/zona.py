from odoo import fields, models, api


class BangunanZona(models.Model):
    _name = 'bangunan.zona'
    _description = 'Bangunan Zona Model'

    name = fields.Char(string='Bangunan Zona Nama', required=True)
    kode = fields.Char(string='Bangunan Zona Kode')
    area_id = fields.Many2one('bangunan.area', string='Bangunan Zona Area ID')
