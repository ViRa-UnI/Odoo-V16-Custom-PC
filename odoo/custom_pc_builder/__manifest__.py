{
    'name': 'Custom PC Builder',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Custom PC Building Module for Odoo V16 CE eCommerce Website',
    'sequence': 1,
    'description': """
    This module allows customers to build and customize their PCs according to their needs.
    Features include:
    - Custom PC Building Interface
    - Component Compatibility Check
    - Predefined Templates
    - Real-time Inventory Check
    - Checkout Integration
    - Security Access
    """,
    'website': 'https://www.yourwebsite.com',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/pc_builder_view.xml',
        'views/component_view.xml',
        'views/template_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}