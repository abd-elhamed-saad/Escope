# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_sample = fields.Boolean(string="Is a Sample", default=False)


class PurchaseOrderSample(models.Model):
    _name = 'purchase.order.sample'
    _inherit = 'purchase.order'
    _description = 'Purchase Order Sample'

    is_sample = fields.Boolean("Is a Sample", default=True)

    # new_sequence = fields.Char(string='New Sequence', required=True, copy=False, index=True,
    #                            default=lambda self: self.env['ir.sequence'].next_by_code('simple.purchase.order'))

    # # Exclude the original sequence field from copying
    # def copy(self, default=None):
    #     default = dict(default or {})
    #     default['new_sequence'] = self.env['ir.sequence'].next_by_code('simple.purchase.order')
    #     return super(PurchaseOrderSample, self).copy(default)
