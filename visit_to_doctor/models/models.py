# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
    _name = 'user.visit'
    _description = 'Visit'

    doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    description = fields.Text(string='Description')
    start_time = fields.Datetime(string='Start Time', readonly=True, )
    end_time = fields.Datetime(string='End Time', readonly=True, )
    state = fields.Selection(string="State", selection=[('new', 'New'), ('followup', 'Follow Up'), ], required=False, )

    def button_end_time(self):
        self.end_time = fields.Datetime.now()

    def button_start_time(self):
        self.start_time = fields.Datetime.now()
