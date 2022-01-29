from odoo import models, fields


class exercise2(models.Model):
    _inherit = 'product.product'
    _description = 'adding minimum age to the products'
    min_age = fields.Integer()

