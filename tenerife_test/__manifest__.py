# -*- coding: utf-8 -*-
{
    'name': "tenerife_test",

    'summary': """
        Módulo de desarrollo de la prueba técnica para la vacante de desarrollador Odoo en Grupo Tenerife""",

    'description': """
        Módulo consiste en desarrollar un módulo personalizado en Odoo:.
    """,

    'author': "Manuel Cuellar",
    'website': "https://www.linkedin.com/in/manuelcuellarr/",


    'category': 'Hidden/Tools',
    'version': '0.1',

    'depends': ['base','product','sale','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_inherit.xml',
        'views/product_label.xml',
        'wizard/wizard_product.xml',
        'reports/product_report.xml',
    ],
}