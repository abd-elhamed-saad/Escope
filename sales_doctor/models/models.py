# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

from datetime import date , datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

SALE_ORDER_STATE = [
    ('draft', "Reception"),
    ('sent', "Reception Sent"),
    ('inter_telescope', "Inter Telescope"),
    ('wake_up', "Wake Up"),
    ('exit_telescope', "Exit Telescope"),
    ('sale', "Sales Order"),
    ('cancel', "Cancelled"),
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    doctor_sale_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])

    state = fields.Selection(selection=SALE_ORDER_STATE, string="Status", readonly=True, copy=False, index=True,
                             tracking=3, default='draft')

    # Add new date fields for each of the new states
    wake_up_date = fields.Datetime(string="Wake Up Date", readonly=True)
    inter_telescope_date = fields.Datetime(string="Inter Telescope Date", readonly=True)
    exit_telescope_date = fields.Datetime(string="Exit Telescope Date", readonly=True)

    def action_wake_up(self):
        self.ensure_one()
        self.write({'state': 'wake_up', 'wake_up_date': fields.Datetime.now()})

    def action_inter_telescope(self):
        self.ensure_one()
        self.write({'state': 'inter_telescope', 'inter_telescope_date': fields.Datetime.now()})

    def action_exit_telescope(self):
        self.ensure_one()
        self.write({'state': 'exit_telescope', 'exit_telescope_date': fields.Datetime.now()})

    def action_confirm(self):
        if self.state not in ['exit_telescope']:
            raise UserError("Order can only be confirmed After Exit Telescope states.")
        super(SaleOrder, self).action_confirm()

    def _can_be_confirmed(self):
        self.ensure_one()
        return self.state in {'draft', 'sent', 'exit_telescope'}
        super()._can_be_confirmed()


class ResPartner(models.Model):
    _inherit = 'res.partner'

    nationality_cust = fields.Char(string="Nationality", )
    is_doctor = fields.Boolean(string='Is Doctor')
    birth_date = fields.Date(string="Date of Birth", tracking=True, )
    member_age = fields.Char(string="Full Age", store=True)
    doctor = fields.Many2one('res.partner', related="sale_order_ids.doctor_sale_id", string="Doctor")
    nationality_country_id = fields.Many2one('res.country', string='Nationality')

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        # البحث باستخدام الاسم الافتراضي
        res = super(ResPartner, self).name_search(name, args=args, operator=operator, limit=limit)

        if not res:
            # البحث باستخدام رقم الهاتف
            partners = self.search([('phone', operator, name)] + args, limit=limit)
            res = partners.name_get()

        return res

    @api.onchange('birth_date')
    def _onchange_birth_date(self):
        if self.birth_date:
            rd = relativedelta(date.today(), self.birth_date)
            self.member_age = str(rd.years) + ' Years & ' + str(rd.months) + ' Months & ' + str(
                rd.days) + ' Days'


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
