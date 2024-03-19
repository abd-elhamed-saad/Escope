# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

SALE_ORDER_STATE = [
    ('draft', "Reception"),
    ('sent', "Scope Sent"),
    ('sale', "Pre Recovery"),
    ('endoscopy', "Endoscopy"),
    ('post_recovery', "Post Recovery"),
    ('dis_change', "Discharge"),
    ('cancel', "Cancelled"),
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection=SALE_ORDER_STATE, string="Status", readonly=True, copy=False, index=True,
                             tracking=3, default='draft')
    doctor_sale_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    endoscopy_date = fields.Datetime(string="Endoscopy Date", readonly=True)
    post_recovery_date = fields.Datetime(string="Post Recovery Date", readonly=True)
    dis_change_date = fields.Datetime(string="Discharge Date", readonly=True)

    medical_endoscope_id = fields.Many2one('medical.endoscopes', string='Related Endoscope')
    medical_endoscope_count = fields.Integer(string='Endoscope Count', compute='_compute_medical_endoscope_count')

    draft_date = fields.Datetime(string="Draft Date",)

    to_endoscopy = fields.Char(string="Endoscopy", compute='_compute_durations', )
    to_post_recovery = fields.Char(string="Post Recovery", compute='_compute_durations', )
    to_discharge = fields.Char(string="Discharge", compute='_compute_durations', )

    def action_create_medical_endoscopes(self):
        self.ensure_one()
        medical_endoscope_rec = self.env['medical.endoscopes'].create({
            'doctor_id': self.doctor_sale_id.id,
            'patient_id': self.partner_id.id,
            'sale_order_id': self.id,
            # Add more fields as needed
        })
        # Redirect to the newly created medical endoscopes record
        return {
            'type': 'ir.actions.act_window',
            'name': 'Medical Endoscopes',
            'view_mode': 'form',
            'res_model': 'medical.endoscopes',
            'res_id': medical_endoscope_rec.id,
            'target': 'current',
        }

    @api.depends('medical_endoscope_id')
    def _compute_medical_endoscope_count(self):
        for record in self:
            related_endoscopes = self.env['medical.endoscopes'].search([('sale_order_id', '=', record.id)])
            record.medical_endoscope_count = len(related_endoscopes)

    def action_view_medical_endoscopes(self):
        self.ensure_one()
        # Your action logic here, typically returning an action dictionary
        return {
            'type': 'ir.actions.act_window',
            'name': 'Related Endoscopes',
            'view_mode': 'tree,form',
            'res_model': 'medical.endoscopes',
            'domain': [('sale_order_id', '=', self.id)],
            'context': "{'create': False}",
        }

    def action_confirm(self):
        for order in self:
            if order.state == 'draft':
                order.draft_date = fields.Datetime.now()
        super(SaleOrder, self).action_confirm()

    def action_endoscopy(self):
        self.ensure_one()
        self.write({'state': 'endoscopy', 'endoscopy_date': fields.Datetime.now()})

    def action_post_recovery(self):
        self.ensure_one()
        self.write({'state': 'post_recovery', 'post_recovery_date': fields.Datetime.now()})

    def action_discharge(self):
        self.ensure_one()
        self.write({'state': 'dis_change', 'dis_change_date': fields.Datetime.now()})

    @api.depends('endoscopy_date', 'draft_date', 'post_recovery_date', 'dis_change_date')
    def _compute_durations(self):
        for record in self:
            # Compute duration from draft to endoscopy
            if record.endoscopy_date and record.draft_date:
                delta = record.endoscopy_date - record.draft_date
                record.to_endoscopy = '%d hours, %d minutes, %d seconds' % (
                    delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)
            else:
                record.to_endoscopy = "Not available"

            # Compute duration from endoscopy to post recovery
            if record.post_recovery_date and record.endoscopy_date:
                delta = record.post_recovery_date - record.endoscopy_date
                record.to_post_recovery = '%d hours, %d minutes, %d seconds' % (
                    delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)
            else:
                record.to_post_recovery = "Not available"

            # Compute duration from post recovery to discharge
            if record.dis_change_date and record.post_recovery_date:
                delta = record.dis_change_date - record.post_recovery_date
                record.to_discharge = '%d hours, %d minutes, %d seconds' % (
                    delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)
            else:
                record.to_discharge = "Not available"
