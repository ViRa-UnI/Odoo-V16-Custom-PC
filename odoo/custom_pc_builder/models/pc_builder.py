```python
from odoo import models, fields, api

class PcBuilder(models.Model):
    _name = 'pc.builder'
    _description = 'PC Builder'

    name = fields.Char(string='Name', required=True)
    components = fields.Many2many('pc.component', string='Components')
    total_price = fields.Float(string='Total Price', compute='_compute_total_price')
    template_id = fields.Many2one('pc.template', string='Template')

    @api.depends('components')
    def _compute_total_price(self):
        for record in self:
            record.total_price = sum(component.price for component in record.components)

    @api.constrains('components')
    def _check_component_compatibility(self):
        for record in self:
            if not record._are_components_compatible():
                raise ValidationError("The selected components are not compatible.")

    def _are_components_compatible(self):
        # Implement the logic to check the compatibility of the components
        pass

    @api.onchange('template_id')
    def _onchange_template_id(self):
        if self.template_id:
            self.components = self.template_id.components
```
