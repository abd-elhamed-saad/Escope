# -*- coding: utf-8 -*-
{
    'name': "Visit To Doctor",
    'summary': """""",
    'description': """""",
    'author': "Abd Elhamed Saad",
    'website': "https://www.linkedin.com/in/abd-elhamed-saad/",
    'category': 'Services',
    'version': '1.0',
    'license': "LGPL-3",
    'depends': ['base', 'sales_doctor', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/doctor_partner.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
