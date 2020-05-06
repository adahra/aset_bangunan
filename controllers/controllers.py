# -*- coding: utf-8 -*-
from odoo import http


class AsetBangunan(http.Controller):

    @http.route('/bangunan/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/bangunan/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bangunan.listing', {
            'root': '/bangunan',
            'objects': http.request.env['bangunan.bangunan'].search([]),
        })

    @http.route('/bangunan/objects/<model("bangunan.bangunan"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('bangunan.object', {
            'object': obj
        })
