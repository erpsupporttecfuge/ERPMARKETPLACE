# -*- coding: utf-8 -*-
{
    'name': "Market Place Customisation",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Tecfuge",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','purchase','stock'],

    # always loaded
    'data': [
        'security/security.xml',
        'data/company_user_create_mail_template.xml',
        'views/company.xml',
        'views/product.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

