from odoo import fields, models, api


class BangunanBangunan(models.Model):
    _name = 'bangunan.bangunan'
    _description = 'Bangunan Bangunan Model'

    name = fields.Char(string='Bangunan Nama', required=True)
    kode = fields.Char(string='Bangunan Kode')
    area_id = fields.Many2one('bangunan.area', string='Bangunan Area ID')
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
