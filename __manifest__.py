# -*- coding: utf-8 -*-
{
    'name': "Show DB Name",

    'summary': """
        Show the database name on the top right of web page without needing to debug mode.""",

    'description': """
        By Installing this module, you will be able To see the database name on the top right of web page without needing to debug mode.
    """,

    'author': "Mint System GmbH",
    'website': "http://mint-system.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        'views/show_db_name_views.xml',
    ],
}
