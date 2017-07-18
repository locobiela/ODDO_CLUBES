# -*- coding: utf-8 -*-
{
    'name': "Padron de Socios",

    'summary': """
        Gestion de socios para Radioclubes""",

    'description': """
        Modulo que gestiona socios de Radioclubes.
        altas, bajas y modificaciones del padron
    """,

    'author': "Leandro A. Masutti",
    'website': "http://www.sart.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Educacion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'padron_socios.xml',
        'padron_cuentas.xml',
            ],
}