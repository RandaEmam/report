# -*- coding: utf-8 -*-
{
    'name': "Quotation and invoice report",

    'summary': """

        Quotation and invoice report

        """,

    'description': """
       customization in quotation and invoice reports
    """,

    'author': "Randa Emam <<eng.randa90@gmail.com>>",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale','account'],

    # always loaded
    'data': [

        'views/product_inherit.xml',
        'report/quotation_report.xml',
        'report/invoice_report.xml'

    ],


}