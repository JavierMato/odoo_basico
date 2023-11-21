# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo informacion'
    _sql_constraints = [('nomeUnico', 'unique(name)', 'Non se pode repetir o nome')]
    _order = "descripcion desc"

    name = fields.Char(required=True, size=20, string="Titulo:")
    descripcion = fields.Text(string="A descripción:")
    alto_en_cm = fields.Integer(string="Alto en centímetros:")
    longo_en_cm = fields.Integer(string="Longo en centímetros:")
    ancho_en_cm = fields.Integer(string="Ancho en centímetros:")
    volume = fields.Float(digits=(6,7), compute="_volume", store=True, string="Volume m3")
    literal = fields.Char(store=False)
    peso = fields.Float(digits=(6,2), default = 2.7, string="Peso en KG.:")
    densidade = fields.Float(compute="_densidade", store=True, string="Densidade en KG/m3:")
    autorizado = fields.Boolean(default=True, string="¿Autorizado?")
    sexo_traducido = fields.Selection([('Hombre','Home'),('Mujer','Muller'),('Otros','Outros')], string="Sexo:")

    @api.depends('alto_en_cm', 'longo_en_cm', 'ancho_en_cm')
    def _volume(self):
        for rexistro in self:
            rexistro.volume = (float(rexistro.alto_en_cm) * float(rexistro.longo_en_cm) * float(rexistro.ancho_en_cm))/1000000

    @api.depends('volume', 'peso')
    def _densidade(self):
        for rexistro in self:
            if rexistro.volume != 0:
                rexistro.densidade = float(rexistro.peso) / float(rexistro.volume)
            else:
                rexistro.densidade = 0

    @api.onchange('alto_en_cm')
    def _avisoAlto(self):
        for rexistro in self:
            if rexistro.alto_en_cms > 7:
                rexistro.literal = 'O alto ten un valor posiblemente excesivo %s é maior que 7' % rexistro.alto_en_cm
            else:
                rexistro.literal = ""

    @api.constrains('peso')  # Ao usar ValidationError temos que importar a libreria ValidationError
    def _constrain_peso(self):  # from odoo.exceptions import ValidationError
        for rexistro in self:
            if rexistro.peso < 1 or rexistro.peso > 4:
                raise ValidationError('Os peso de %s ten que ser entre 1 e 4 ' % rexistro.name)

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
