from odoo import models, fields, api
from odoo.exceptions import ValidationError


class exercise3(models.Model):
    _inherit = 'sale.order.line'
    _description = 'adding date of birth and min age to each order line'

    min_age = fields.Integer(related='product_id.min_age', store=True)
    age = fields.Integer(related='order_id.partner_id.age', store=True)

    @api.constrains('min_age', 'dob')
    def check_age(self):
        # import ipdb
        # ipdb.set_trace()
        for record in self:
            if record.min_age > record.age:
                raise ValidationError("Customer can not purchase this item due to age restriction")
