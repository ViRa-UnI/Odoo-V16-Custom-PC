```python
from odoo import models, fields

class Template(models.Model):
    _name = 'pc.builder.template'
    _description = 'PC Builder Template'

    name = fields.Char(string='Template Name', required=True)
    description = fields.Text(string='Description')
    components = fields.Many2many('pc.builder.component', string='Components')
    price = fields.Float(compute='_compute_price', string='Total Price', store=True)

    def _compute_price(self):
        for record in self:
            record.price = sum(component.price for component in record.components)
```