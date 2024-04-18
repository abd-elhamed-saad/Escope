# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerDoctor(models.Model):
    _inherit = 'res.partner'

    create_time = fields.Datetime(string="Creation Time", compute="_compute_create_time", store=True, readonly=True,
                                  copy=False)
    end_visit_time = fields.Datetime(string="End Visit Time", readonly=True, copy=False)
    is_discount = fields.Boolean(string="Apply Discount")
    discount_rate = fields.Float(string="Discount Percentage")

    @api.depends('name')
    def _compute_create_time(self):
        for record in self:
            if record.name and not record.create_time:
                record.create_time = fields.Datetime.now()

    def button_end_visit(self):
        self.end_visit_time = fields.Datetime.now()


class AccountMove(models.Model):
    _inherit = 'account.move'

    doctor_dis_id = fields.Many2one('res.partner', string='Doctor Discount',
                                    domain=[('is_discount', '=', True)])
    doctor_discount = fields.Float(string="Doctor Discount", compute="_compute_doctor_discount", store=True)

    @api.depends('doctor_dis_id')
    def _compute_doctor_discount(self):
        for move in self:
            if move.doctor_dis_id and move.doctor_dis_id.is_discount:
                move.doctor_discount = move.doctor_dis_id.discount_rate * 100
            else:
                move.doctor_discount = 0.0

    @api.onchange('doctor_dis_id')
    def _apply_discount_to_lines(self):
        if self.doctor_discount > 0:
            for line in self.invoice_line_ids:
                line.discount = self.doctor_discount
