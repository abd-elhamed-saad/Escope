# -*- coding: utf-8 -*-
{
    'name': "Purchase Inherit",
    'summary': """    """,
    'description': """   """,
    'author': "Abd El-hamed Saad",
    'website': "http://www.MyCompany.co",
    'category': 'Uncategorized',
    'version': '0.16',
    'license': 'LGPL-3',
    'application': True,
    'auto_install': False,
    'depends': ['base', 'purchase','account' ],
    'data': [
        'security/ir.model.access.csv',
        'data/new_purchase_data.xml',
        'views/new_purchase_view.xml',
        'views/views.xml',

    ],
}
