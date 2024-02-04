# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean(string='Is Doctor')
    birth_date = fields.Date(string="Date of Birth", tracking=True, required=True)
    member_age = fields.Char(string="Full Age", store=True)
    doctor = fields.Many2one('res.partner', related="sale_order_ids.doctor_sale_id", string="Doctor")

    @api.onchange('birth_date')
    def _onchange_birth_date(self):
        if self.birth_date:
            rd = relativedelta(date.today(), self.birth_date)
            self.member_age = str(rd.years) + ' Years & ' + str(rd.months) + ' Months & ' + str(
                rd.days) + ' Days'


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    doctor_sale_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])


class SaleReportDoc(models.Model):
    _inherit = 'sale.report'

    doctor_sale_id = fields.Many2one('res.partner', string="Doctor", readonly=True)

    class SaleReport(models.Model):
        _inherit = 'sale.report'

        doctor_sale_id = fields.Many2one('res.partner', string="Doctor", readonly=True)

        def _select_additional_fields(self):
            res = super()._select_additional_fields()
            res['doctor_sale_id'] = "s.doctor_sale_id"
            return res

        def _group_by_sale(self):
            res = super()._group_by_sale()
            res += """,
                s.doctor_sale_id"""
            return res

        # def _select(self):
        #     return super(SaleReportDoc, self)._select() + ", so.doctor_sale_id as doctor_sale_id"
        #
        # def _group_by(self):
        #     return super(SaleReportDoc, self)._group_by() + ", so.doctor_sale_id"

    # def _select(self):
    #     return super(SaleReportDoc, self)._select() + ", s.doctor_sale_id as doctor_sale_id"
    #
    # def _group_by(self):
    #     return super(SaleReportDoc, self)._group_by() + ", s.doctor_sale_id"
    #
    # @api.model
    # def _get_groupby_mapping(self):
    #     groupby_mapping = super(SaleReportDoc, self)._get_groupby_mapping()
    #     groupby_mapping.update({
    #         'doctor_sale_id': 's.doctor_sale_id',
    #     })
    #     return groupby_mapping
