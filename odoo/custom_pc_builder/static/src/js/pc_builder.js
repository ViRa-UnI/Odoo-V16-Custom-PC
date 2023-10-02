odoo.define('custom_pc_builder.pc_builder', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');

    var PcBuilder = Widget.extend({
        template: 'custom_pc_builder.pc_builder',
        events: {
            'dragstart .component': 'dragStart',
            'dragover .dropzone': 'dragOver',
            'drop .dropzone': 'drop',
            'click .remove-component': 'removeComponent',
            'click .predefined-template': 'loadTemplate',
            'click .checkout': 'checkout',
        },

        init: function (parent, options) {
            this._super(parent, options);
            this.components = [];
            this.totalPrice = 0;
        },

        start: function () {
            this.updatePrice();
            this.checkInventory();
        },

        dragStart: function (event) {
            event.originalEvent.dataTransfer.setData('text/plain', event.target.dataset.id);
        },

        dragOver: function (event) {
            event.preventDefault();
        },

        drop: function (event) {
            event.preventDefault();
            var componentId = event.originalEvent.dataTransfer.getData('text/plain');
            this.addComponent(componentId);
        },

        addComponent: function (componentId) {
            var self = this;
            ajax.jsonRpc('/pc_builder/component/' + componentId, 'call').then(function (component) {
                if (self.checkCompatibility(component)) {
                    self.components.push(component);
                    self.updatePrice();
                    self.checkInventory();
                } else {
                    alert('The selected component is not compatible with the other components.');
                }
            });
        },

        removeComponent: function (event) {
            var componentId = $(event.target).data('id');
            this.components = this.components.filter(function (component) {
                return component.id !== componentId;
            });
            this.updatePrice();
            this.checkInventory();
        },

        loadTemplate: function (event) {
            var templateId = $(event.target).data('id');
            var self = this;
            ajax.jsonRpc('/pc_builder/template/' + templateId, 'call').then(function (template) {
                self.components = template.components;
                self.updatePrice();
                self.checkInventory();
            });
        },

        checkout: function () {
            ajax.jsonRpc('/pc_builder/checkout', 'call', {
                components: this.components.map(function (component) {
                    return component.id;
                }),
            }).then(function (result) {
                if (result.success) {
                    window.location.href = '/shop/checkout';
                } else {
                    alert('An error occurred during the checkout process.');
                }
            });
        },

        checkCompatibility: function (newComponent) {
            // Implement the logic to check the compatibility of the new component with the existing components.
            return true;
        },

        updatePrice: function () {
            this.totalPrice = this.components.reduce(function (total, component) {
                return total + component.price;
            }, 0);
            this.$('.total-price').text(this.totalPrice);
        },

        checkInventory: function () {
            // Implement the logic to check the inventory of the components and update the UI accordingly.
        },
    });

    core.action_registry.add('pc_builder', PcBuilder);

    return PcBuilder;
});