# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerDoctor(models.Model):
    _inherit = 'res.partner'

    create_time = fields.Datetime(string="Creation Time", compute="_compute_create_time", store=True, readonly=True,
                                  copy=False)
    end_visit_time = fields.Datetime(string="End Visit Time", readonly=True, copy=False)

    @api.depends('name')
    def _compute_create_time(self):
        for record in self:
            if record.name and not record.create_time:
                record.create_time = fields.Datetime.now()

    def button_end_visit(self):
        self.end_visit_time = fields.Datetime.now()

    # create_time = fields.Datetime(string="Creation Time", readonly=True, copy=False)
    # end_visit_time = fields.Datetime(string="End Visit Time", readonly=True, copy=False)
    #
    # @api.model
    # def create(self, vals):
    #     vals['create_time'] = fields.Datetime.now()
    #     return super(PartnerDoctor, self).create(vals)
    #
    # def button_end_visit(self):
    #     self.end_visit_time = fields.Datetime.now()
