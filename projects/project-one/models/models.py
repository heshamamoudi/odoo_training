# -*- coding: utf-8 -*-


from odoo import models, fields


class Project_one(models.Model):
    _name = 'first.training.model'
    _description = 'project-one.project-one'
    name = fields.Char()
    age = fields.Integer()
