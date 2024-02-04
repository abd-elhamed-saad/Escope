# -*- coding: utf-8 -*-
{
    'name': "sales_doctor",
    'summary': """    """,
    'description': """   """,
    'author': "Abd El-hamed Saad",
    'website': "http://www.MyCompany.co",
    'category': 'Uncategorized',
    'version': '0.16',
    'license': "AGPL-3",
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base', 'sale_management', 'sale'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
