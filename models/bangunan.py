from odoo import fields, api, _
from . import zona


class BangunanBangunan(zona.BangunanZona):
    _name = 'bangunan.bangunan'
    _description = 'Bangunan Bangunan Model'

    @api.multi
    def open_bangunan_lantai(self):
        return {
            'name': _('Lantai'),
            'domain': [('bangunan_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'bangunan.lantai',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def get_lantai_count(self):
        count = self.env['bangunan.lantai'].search_count([('bangunan_id', '=', self.id)])
        self.lantai_count = count

    zona_id = fields.Many2one('bangunan.zona', string='Bangunan Zona ID')
    jenis_bangunan = fields.Selection([
        ('kantor', 'Kantor'),
        ('sekolah', 'Sekolah'),
        ('ibadah', 'Ibadah'),
        ('sosial', 'Sosial'),
    ], string='Bangunan Jenis Bangunan', default='kantor')
    nomor_imb = fields.Text(string='Bangunan Nomor IMB')
    alamat = fields.Text(string='Bangunan Alamat')
    sertifikat = fields.Selection([
        ('shm', 'SHM'),
        ('shgb', 'SHGN'),
    ], string='Bangunan Sertifikat', default='shm')
    nomor_sertifikat = fields.Text(string='Bangunan Nomor Sertifikat')
    keterangan = fields.Text(string='Bangunan Keterangan')
    lantai_count = fields.Integer(string='Lantai', compute='get_lantai_count')
