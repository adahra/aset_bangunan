from odoo import fields
from . import bangunan


class BangunanLantai(bangunan.BangunanBangunan):
    _name = 'bangunan.lantai'
    _description = 'Bangunan Lantai Model'

    bangunan_id = fields.Many2one('bangunan.bangunan', string='Bangunan ID')
