```python
from odoo.tests import common

class TestPcBuilder(common.TransactionCase):

    def setUp(self):
        super(TestPcBuilder, self).setUp()
        self.PcBuilder = self.env['pc.builder']
        self.Component = self.env['component']
        self.Template = self.env['template']

    def test_create_pc_builder(self):
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
        })
        self.assertEqual(pc_builder.name, 'Test PC Builder')

    def test_create_component(self):
        component = self.Component.create({
            'name': 'Test Component',
            'price': 100.0,
        })
        self.assertEqual(component.name, 'Test Component')
        self.assertEqual(component.price, 100.0)

    def test_create_template(self):
        template = self.Template.create({
            'name': 'Test Template',
        })
        self.assertEqual(template.name, 'Test Template')

    def test_add_component_to_pc_builder(self):
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
        })
        component = self.Component.create({
            'name': 'Test Component',
            'price': 100.0,
        })
        pc_builder.component_ids = [(4, component.id)]
        self.assertEqual(len(pc_builder.component_ids), 1)
        self.assertEqual(pc_builder.component_ids[0].id, component.id)

    def test_remove_component_from_pc_builder(self):
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
        })
        component = self.Component.create({
            'name': 'Test Component',
            'price': 100.0,
        })
        pc_builder.component_ids = [(4, component.id)]
        pc_builder.component_ids = [(3, component.id)]
        self.assertEqual(len(pc_builder.component_ids), 0)

    def test_add_template_to_pc_builder(self):
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
        })
        template = self.Template.create({
            'name': 'Test Template',
        })
        pc_builder.template_ids = [(4, template.id)]
        self.assertEqual(len(pc_builder.template_ids), 1)
        self.assertEqual(pc_builder.template_ids[0].id, template.id)

    def test_remove_template_from_pc_builder(self):
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
        })
        template = self.Template.create({
            'name': 'Test Template',
        })
        pc_builder.template_ids = [(4, template.id)]
        pc_builder.template_ids = [(3, template.id)]
        self.assertEqual(len(pc_builder.template_ids), 0)
```