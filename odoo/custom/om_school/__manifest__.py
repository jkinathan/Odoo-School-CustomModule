# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School Management',
    'description': """
Basic Starter Custom Module for School
===============================================
    """,
    'summary': 'School Management Software',
    'version': '1.0',
    'category': 'Productivity',
    'auto_install': False,
    'sequence': -100,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/student.xml'
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
