from odoo import fields, models


class BangunanArea(models.Model):
    _name = 'bangunan.area'
    _description = 'Bangunan Area Model'

    name = fields.Char(string='Bangunan Area Nama', required=True)
    kode = fields.Char(string='Bangunan Area Kode')
