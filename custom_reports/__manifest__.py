# -*- coding: utf-8 -*-
{
    'name': "custom_reports",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "M.Rizwan ",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale', 'purchase', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order_report.xml',
        'views/purchasequotation_report.xml',
        'views/sale_order_report.xml',
        'views/invoice_report.xml',
        'views/delivery_slip_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
