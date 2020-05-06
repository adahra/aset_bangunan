from odoo import fields, models


class BangunanLantai(models.Model):
    _name = 'bangunan.lantai'
    _description = 'Bangunan Lantai Model'

    name = fields.Char(string='Bangunan Lantai Nama', required=True)
    kode = fields.Char(string='Bangunan Lantai Kode')
    bangunan_id = fields.Many2one('bangunan.bangunan', string='Bangunan ID')
