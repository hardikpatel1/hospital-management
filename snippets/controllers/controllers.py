# -*- coding: utf-8 -*-
from odoo import http

# class Snippets(http.Controller):
#     @http.route('/snippets/snippets/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/snippets/snippets/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('snippets.listing', {
#             'root': '/snippets/snippets',
#             'objects': http.request.env['snippets.snippets'].search([]),
#         })

#     @http.route('/snippets/snippets/objects/<model("snippets.snippets"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('snippets.object', {
#             'object': obj
#         })