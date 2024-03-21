# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_sample = fields.Boolean(string="Is a Sample", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('is_sample'):
                vals['name'] = self.env['ir.sequence'].next_by_code('simple.inherit.purchase') or 'New'
            res = super(PurchaseOrder, self).create(vals)
        return res
