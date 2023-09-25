```python
from odoo import models, fields

class Component(models.Model):
    _name = 'custom_pc_builder.component'
    _description = 'PC Component'

    name = fields.Char(string='Component Name', required=True)
    component_type = fields.Selection([
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('other', 'Other')
    ], string='Component Type', required=True)
    price = fields.Float(string='Price', required=True)
    inventory = fields.Integer(string='Inventory', required=True)
    compatible_with = fields.Many2many('custom_pc_builder.component', 'component_compatibility_rel', 'component_id', 'compatible_id', string='Compatible Components')

    def check_compatibility(self, component):
        return component in self.compatible_with
```