from odoo import models, fields, api
class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    _description = 'Herencia del modelo Product Template'

    x_sales_count = fields.Integer(
        string="Ventas",
        compute="_x_compute_sales_count"
    )
    x_description_product = fields.Text(
        string='Descripción del Prodcuto')
    
    x_product_label_ids = fields.Many2many(
        comodel_name='product.label', 
        string='Etiquetas')
    

    def _x_compute_sales_count(self):
        for product in self:
            sale_lines = self.env['sale.order.line'].search([
                ('product_id', 'in', product.product_variant_ids.ids),
                ('state', 'in', ['sale', 'done']),
            ])

            order_ids = sale_lines.mapped('order_id').ids
            product.x_sales_count = len(order_ids)

    def action_open_sales_list(self):
        self.ensure_one()
        sale_lines = self.env['sale.order.line'].search([
            ('product_id', 'in', self.product_variant_ids.ids),
            ('state', 'in', ['sale', 'done']),
        ])
        orders = sale_lines.mapped('order_id')
        
        action = {
            'type': 'ir.actions.act_window',
            'name': f'Órdenes de Venta ({self.name})',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', orders.ids)],
            'context': {
                'create': False,
            },
        }
        return action