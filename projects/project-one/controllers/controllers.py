# -*- coding: utf-8 -*-
# from odoo import http


# class Project-one(http.Controller):
#     @http.route('/project-one/project-one', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-one/project-one/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-one.listing', {
#             'root': '/project-one/project-one',
#             'objects': http.request.env['project-one.project-one'].search([]),
#         })

#     @http.route('/project-one/project-one/objects/<model("project-one.project-one"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-one.object', {
#             'object': obj
#         })
