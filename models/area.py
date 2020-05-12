from odoo import fields, models, api, _


class BangunanArea(models.Model):
    _name = 'bangunan.area'
    _description = 'Bangunan Area Model'
    _rec_name = 'name'

    @api.model
    def create(self, vals):
        if vals.get('kode', _('New')) == _('New'):
            vals['kode'] = self.env['ir.sequence'].next_by_code('bangunan.area.sequence') or _('New')
        return super(BangunanArea, self).create(vals)

    name = fields.Char(string='Nama', required=True)
    # kode = fields.Char(string='Bangunan Area Kode')
    kode = fields.Char(string='Kode', required=True, copy=False,
                       readonly=True, index=True, default=lambda self: _('New'))
