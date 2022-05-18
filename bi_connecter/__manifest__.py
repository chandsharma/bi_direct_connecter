# -*- coding: utf-8 -*-
{
    'name': "Power BI Direct Connector",

    'summary': """
       Connects your Odoo directly to Power BI Desktop. This is Direct Odoo Power BI Connector with Updated Features. Make Power BI Dashboard, Power BI Dashboards, Power BI report, Power BI Reports easily. Get automatic scheduled data refresh. Odoo to Power BI . With many advanced features like, publishing dashboard to Microsoft Teams or Publically, Automatically scheduled refresh / reload, gateway support, Get Prebuilt tables relationship. This is fast connector to link your data from odoo to Business Intelligence tool (Power BI Desktop). With ER diagram like features get relation / relations and relationship of your tables and get related column data. powerbi , business intelli. powerbi connector, odoo to powerbi connector , odoo powerbi connection, odoo power bi connection. Odoo ERP.  Odoo Dashboard, CRM Dashboard, Inventory Dashboard, Sales Dashboard, Account Dashboard, Invoice Dashboard, Revamp Dashboard, Best Dashboard, Odoo Best Dashboard, Odoo Apps Dashboard, Best Ninja Dashboard, Analytic Dashboard, Pre-Configured Dashboard, Create Dashboard, Beautiful Dashboard, Customized Robust Dashboard, Predefined Dashboard, Multiple Dashboards, Advance Dashboard, Beautiful Powerful Dashboards, Chart Graphs Table View, All In One Dynamic Dashboard, Accounting Stock Dashboard, Pie Chart Dashboard, Modern Dashboard, Dashboard Studio, Dashboard Builder, Dashboard Designer, Odoo Studio.  Revamp your Odoo Dashboard like never before! It is one of the best dashboard odoo apps in the market. 
       """,
       'description':"""Connects your Odoo directly to Power BI Desktop. This is Direct Odoo Power BI Connector with Updated Features. Make Power BI Dashboard, Power BI Dashboards, Power BI report, Power BI Reports easily. Get automatic scheduled data refresh. Odoo to Power BI . With many advanced features like, publishing dashboard to Microsoft Teams or Publically, Automatically scheduled refresh / reload, gateway support, Get Prebuilt tables relationship. This is fast connector to link your data from odoo to Business Intelligence tool (Power BI Desktop). With ER diagram like features get relation / relations and relationship of your tables and get related column data. powerbi , business intelli. powerbi connector, odoo to powerbi connector , odoo powerbi connection, odoo power bi connection.
     """,
     'live_test_url': 'https://app.powerbi.com/view?r=eyJrIjoiYTc1MDBkY2UtMDQxOC00NDE5LTk2NTEtNGM3MjA3ZTljOTY2IiwidCI6ImI2NzFmYmQxLWUyOTItNDVlZS05MGM2LTgzNjg3MzFlOTFiOCJ9',

    'author': "Techneith",
    'maintainer': 'Techneith',
    'website': "https://www.techneith.com",
    'support': "info@techneith.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1.2',
    'price': 700,
    'currency': 'USD',
    # any module necessary for this one to work correctly
    'depends': ['base',],
    'images': ['static/description/banner.gif'],
    "external_dependencies": {"python" : ["pip"]},
    "license":"LGPL-3",

    # always loaded
    'data': [
        'views/settings.xml',
        # 'views/resources.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "application": True,
    "installable": True,
    "post_init_hook":"bi_post_init_hook",
    "uninstall_hook":"bi_uninstall_hook"
}
