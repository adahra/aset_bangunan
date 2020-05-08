# -*- coding: utf-8 -*-
{
    'name': "Aset Bangunan",

    'summary': """
        Data Bangunan""",

    'description': """
        Master Data Bangunan
    """,

    'author': "Adnanto A.R.",
    'website': "http://adahra.github.io",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/area_data_default.xml',
        'data/zona_data_default.xml',
        'data/bangunan_data_default.xml',
        'data/lantai_data_default.xml',
        'data/ruang_data_default.xml',
        'views/dashboard.xml',
        'views/area.xml',
        'views/zona.xml',
        'views/lantai.xml',
        'views/ruang.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    "auto_install": False,
}
