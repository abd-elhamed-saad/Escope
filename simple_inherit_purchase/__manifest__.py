# -*- coding: utf-8 -*-
{
    'name': "simple Purchase Inherit",
    'summary': """    """,
    'description': """   """,
    'author': "Abd El-hamed Saad",
    'website': "http://www.MyCompany.co",
    'category': 'Uncategorized',
    'version': '0.16',
    'license': 'LGPL-3',
    'application': True,
    'auto_install': False,
    'depends': ['base', 'purchase', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'data/simple_inherit_purchase_sequence.xml',
        'views/simple_inherit_purchase_views.xml',
    ],
}
