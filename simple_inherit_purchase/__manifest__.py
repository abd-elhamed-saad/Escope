# -*- coding: utf-8 -*-
{
    'name': "simple Purchase Inherit",
    'summary': """""",
    'description': """""",
    'author': "Abd Elhamed Saad",
    'website': "https://www.linkedin.com/in/abd-elhamed-saad/",
    'category': 'Services',
    'version': '17.0.1.0',
    'license': "LGPL-3",
    'application': True,
    'auto_install': False,
    'depends': ['base', 'purchase', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/simple_inherit_purchase_sequence.xml',
        'views/simple_inherit_purchase_views.xml',
    ],
}
