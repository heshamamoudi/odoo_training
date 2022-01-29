# -*- coding: utf-8 -*-

from odoo import models, fields, api


class flower_app2(models.Model):
    _inherit = 'product.product'
    _description = 'an app for a flower shop'

    common_name = fields.Char()
    scientific_name = fields.Char()
    season_start = fields.Selection(
        [("jan", "January"), ("feb", "February")])
    season_end = fields.Selection(
        [("dec", "December"), ("may", "May")])
    freq = fields.Integer()
    watering_amount = fields.Float()
    is_flower = fields.Boolean()

    def default_context(self):
        for record in self:
            record.with_context({'is_flower': False})
