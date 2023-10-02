```python
from odoo import http
from odoo.http import request

class CustomPCBuilder(http.Controller):

    @http.route('/pc_builder', type='http', auth='user', website=True)
    def pc_builder(self, **kwargs):
        components = request.env['custom_pc_builder.component'].search([])
        templates = request.env['custom_pc_builder.template'].search([])
        return request.render('custom_pc_builder.pc_builder', {
            'components': components,
            'templates': templates,
        })

    @http.route('/pc_builder/add_component', type='json', auth='user')
    def add_component(self, component_id, **kwargs):
        Component = request.env['custom_pc_builder.component']
        component = Component.browse(int(component_id))
        if not component.exists():
            return {'error': 'Component not found'}
        request.session.setdefault('pc_builder', []).append(component.id)
        return {'total_price': Component.get_total_price(request.session['pc_builder'])}

    @http.route('/pc_builder/remove_component', type='json', auth='user')
    def remove_component(self, component_id, **kwargs):
        Component = request.env['custom_pc_builder.component']
        component = Component.browse(int(component_id))
        if not component.exists():
            return {'error': 'Component not found'}
        request.session.setdefault('pc_builder', []).remove(component.id)
        return {'total_price': Component.get_total_price(request.session['pc_builder'])}

    @http.route('/pc_builder/checkout', type='http', auth='user', website=True)
    def checkout(self, **kwargs):
        PcBuilder = request.env['custom_pc_builder.pc_builder']
        pc_builder = PcBuilder.create_from_session(request.session.get('pc_builder', []))
        return request.redirect('/shop/checkout')
```