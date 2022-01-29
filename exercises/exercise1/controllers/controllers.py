# -*- coding: utf-8 -*-
# from odoo import http


# class Excercose1(http.Controller):
#     @http.route('/excercose1/excercose1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/excercose1/excercose1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('excercose1.listing', {
#             'root': '/excercose1/excercose1',
#             'objects': http.request.env['excercose1.excercose1'].search([]),
#         })

#     @http.route('/excercose1/excercose1/objects/<model("excercose1.excercose1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('excercose1.object', {
#             'object': obj
#         })
