# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date, datetime


class exercise1(models.Model):
    _inherit = 'res.partner'
    _description = 'adding date of birth to each contact'

    date_of_birth = fields.Date()
    age = fields.Integer(compute='comp_age')

    @api.onchange('date_of_birth')
    def comp_age(self):
        age = ''
        today_date = date.today()
        for record in self:
            if record.date_of_birth:
                dt = str(record.date_of_birth)
                year = datetime.today().year - record.date_of_birth.year
                record.age = year
