# -*- coding: utf-8 -*-
# from odoo import http


# class FlowerApp1(http.Controller):
#     @http.route('/flower_app1/flower_app1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flower_app1/flower_app1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('flower_app1.listing', {
#             'root': '/flower_app1/flower_app1',
#             'objects': http.request.env['flower_app1.flower_app1'].search([]),
#         })

#     @http.route('/flower_app1/flower_app1/objects/<model("flower_app1.flower_app1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flower_app1.object', {
#             'object': obj
#         })
