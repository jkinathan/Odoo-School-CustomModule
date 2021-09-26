# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Student"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        
    ], required=True, default='male')
    note = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
