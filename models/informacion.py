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
    volume = fields.Float(compute="_volume", store=True)
    literal = fields.Char(store=False)
    peso = fields.Float(digits=(6,2), default = 2.7, string="Peso en KG.:")
    autorizado = fields.Boolean(default=True, string="¿Autorizado?")
    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo:")

    @api.depends('alto_en_cm', 'longo_en_cm', 'ancho_en_cm')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = float(rexistro.alto_en_cm) * float(rexistro.longo_en_cm) * float(rexistro.ancho_en_cm)

    @api.onchange('alto_en_cm')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cm
            else:
                rexistro.literal = ""


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
