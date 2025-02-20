# -*- coding: utf-8 -*-
{
    'name': "Sale CRM Won Update",

    'summary': "Update CRM into Won stage when sale order is confirmed",

    'description': """
        Add function to update CRM into Won stage when sale order is confirmed
    """,

    'author': "Chaidar Aji Nugroho",
    # 'website': "https://www.yourcompany.com",

    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'wizards/wizard_sale_crm_won_update_views.xml',
    ],
    'installable': True,
    'application': True,
}

