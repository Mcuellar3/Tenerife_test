# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductLabel(models.Model):
    _name = 'product.label'
    _description = 'Modelo de prueba para grupo Tenerife'

    name = fields.Char(string='Nombre')
    description = fields.Text(string='Descripción')
    