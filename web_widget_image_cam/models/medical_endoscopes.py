from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class MedicalEndoscopes(models.Model):
    _name = 'medical.endoscopes'
    _description = 'Medical Endoscopes'

    name = fields.Char(string='Request Number', required=True, readonly=True, default=lambda self: _('New'), copy=False)

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    image_1 = fields.Binary(string="Image 1", store=True, )
    image_2 = fields.Binary(string="Image 2", store=True, )
    image_3 = fields.Binary(string="Image 3", store=True, )
    image_4 = fields.Binary(string="Image 4", store=True, )
    image_5 = fields.Binary(string="Image 5", store=True, )
    image_6 = fields.Binary(string="Image 6", store=True, )
    image_7 = fields.Binary(string="Image 7", store=True, )
    image_8 = fields.Binary(string="Image 8", store=True, )
    image_9 = fields.Binary(string="Image 9", store=True, )
    image_10 = fields.Binary(string="Image 10", store=True, )
    image_11 = fields.Binary(string="Image 11", store=True, )
    image_12 = fields.Binary(string="Image 12", store=True, )
    image_13 = fields.Binary(string="Image 13", store=True, )
    image_14 = fields.Binary(string="Image 14", store=True, )
    image_15 = fields.Binary(string="Image 15", store=True, )
    doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    operator = fields.Char(string="Operator")
    referred_by = fields.Char(string="Referred By")
    id_patient = fields.Char(string="ID")

    patient_phone = fields.Char(string="Patient Phone", related="patient_id.phone", readonly=True)
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
    indications = fields.Text(string="Indication For Examination")
    procedures = fields.Char(string="Procedures")
    medications = fields.Char(string="Medications")
    findings = fields.Text(string="Findings")
    conclusions = fields.Text(string="Conclusions")
    recommendations = fields.Text(string="Recommendations")
    nurse = fields.Char(string="Nurse")
    nurse_assistant = fields.Char(string="Nursing assistant")
    e_device = fields.Integer(string="E-device")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('medical.endoscopes') or _('New')
        return super(MedicalEndoscopes, self).create(vals_list)

    birth_date = fields.Date(string="Date of Birth", related="patient_id.birth_date")

    # Replace the age field with a computed one
    age = fields.Integer(string="Age", compute="_compute_age_from_birth_date")

    @api.depends('birth_date')
    def _compute_age_from_birth_date(self):
        for record in self:
            if record.birth_date:
                today = datetime.now().date()
                birth_date = fields.Date.from_string(record.birth_date)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0
