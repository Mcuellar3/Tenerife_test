# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductUpdateWizard(models.TransientModel):
    _name = 'product.update.wizard'
    _description = 'Wizard para actualizar etiquetas de productos'

    x_product_ids = fields.Many2many(
        comodel_name='product.template', 
        string='Productos',
        required=True)
    x_label_ids = fields.Many2many(
        comodel_name='product.label', 
        string='Etiqueta',
        required=True)
    
    def update_products(self):
        for product in self.x_product_ids:
            product.write({
                'x_product_label_ids': [(6, 0, self.x_label_ids.ids)]
            })
        return {
            'effect':{
                'fadeout':'slow',
                'message':'Las Etiquetas han sido actualizadas.',
                'type':'rainbow_man',
            }
        }