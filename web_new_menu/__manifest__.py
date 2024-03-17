# -*- coding: utf-8 -*-
{
    'name': "Web New Menu",
    'summary': """""",
    'description': """""",
    'author': "Abd Elhamed Saad",
    'website': "https://www.linkedin.com/in/abd-elhamed-saad/",
    'category': 'Services',
    'version': '17.0.1.0',
    'license': "LGPL-3",
    'depends': ['base', 'web_widget_image_cam'],
    'data': [
        'security/ir.model.access.csv',
        'views/e_device.xml',
        'views/inherit_view_web.xml',
        'views/process_name_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
