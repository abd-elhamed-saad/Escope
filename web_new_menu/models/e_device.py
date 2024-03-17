# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NewModule(models.Model):
    _inherit = 'medical.endoscopes'

    e_device_ids = fields.Many2one('e.device', string='E- Devices')
    process_ids = fields.Many2one('process.name',  string='Process Name')


class EDevice(models.Model):
    _name = 'e.device'
    _description = 'Electronic Device'

    name = fields.Char(string='Device Name', required=True)
    code = fields.Char(string='Device Code', )
    medical_endoscope_id = fields.Many2one('medical.endoscopes', string='Related Endoscope')
    device_line_ids = fields.One2many('e.device.line', 'e_device_id', string='Maintenance Lines')


class EDeviceLine(models.Model):
    _name = 'e.device.line'
    _description = 'Electronic Device Line'

    e_device_id = fields.Many2one('e.device', string='Related Device')
    malfunction = fields.Char(string='العطل')
    malfunction_date = fields.Date(string='تاريخ العطل')
    malfunction_type = fields.Text(string='نوع العطل')
    sent_for_maintenance = fields.Date(string='تاريخ ارسال للصيانة')
    back_from_maintenance = fields.Date(string='والعودة من الصيانة')
    fixed_issues = fields.Text(string='ما تم اصلاخة')
    maintenance_company = fields.Char(string='اسم شركة الصيانة')
    maintenance_cost = fields.Float(string='التكلفة')
    note = fields.Text(string='ملاحظات')


