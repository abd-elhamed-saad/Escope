# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class change_menui_name(models.Model):
#     _name = 'change_menui_name.change_menui_name'
#     _description = 'change_menui_name.change_menui_name'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
