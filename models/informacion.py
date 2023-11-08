# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo informacion'

    name = fields.Char(required=True, size=20, string="Titulo:")
    descripcion = fields.Text(string="A descripción:")
    alto_en_cm = fields.Integer(string="Alto en centímetros:")
    longo_en_cm = fields.Integer(string="Longo en centímetros:")
    ancho_en_cm = fields.Integer(string="Ancho en centímetros:")
    peso = fields.Float(digits=(6,2), default = 2.7, string="Peso en KG.:")



# class odoo_basico(models.Model):
#     _name = 'odoo_basico.odoo_basico'
#     _description = 'odoo_basico.odoo_basico'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
