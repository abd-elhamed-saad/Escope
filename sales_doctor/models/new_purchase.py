# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_sample = fields.Boolean(string="Is a Sample", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        orders = self.browse()
        for vals in vals_list:
            # Determine the appropriate sequence code
            sequence_code = 'purchase.order.sample' if vals.get('is_sample') else 'purchase.order'

            if vals.get('name', 'New') == 'New':
                seq_date = None
                if 'date_order' in vals:
                    seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
                vals['name'] = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=seq_date) or '/'

        return super(PurchaseOrder, self).create(vals_list)


class PurchaseOrderSample(models.Model):
    _name = 'purchase.order.sample'
    _inherit = 'purchase.order'
    _description = 'Purchase Order Sample'

    is_sample = fields.Boolean("Is a Sample", default=True)
