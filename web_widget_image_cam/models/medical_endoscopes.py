from odoo import api, fields, models, _
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import base64


class MedicalEndoscopes(models.Model):
    _name = 'medical.endoscopes'
    _description = 'Medical Endoscopes'

    name = fields.Char(string='Request Number', required=True, readonly=True, default=lambda self: _('New'), copy=False)

    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    video = fields.Binary(string="Video")
    video_data = fields.Char(string="Video Data")

    def save_video(self, video_data):
        print("@@@@@@@@@@@@@_save_video", video_data)
        print("@@@@@@@@@@@@@record_id", )
        video_data_bytes = base64.b64decode(video_data)

        self.write({
            'video_data': 'Video Data Placeholder',  # You can replace this with relevant video metadata
            'video': base64.b64encode(video_data_bytes),  # Store binary data as base64 in the video field
        })

    img1 = fields.Binary(string="Image 1", store=True, )
    img2 = fields.Binary(string="Image 2", store=True, )
    img3 = fields.Binary(string="Image 3", store=True, )
    img4 = fields.Binary(string="Image 4", store=True, )
    img5 = fields.Binary(string="Image 5", store=True, )
    img6 = fields.Binary(string="Image 6", store=True, )
    img7 = fields.Binary(string="Image 7", store=True, )
    img8 = fields.Binary(string="Image 8", store=True, )
    img9 = fields.Binary(string="Image 9", store=True, )
    img10 = fields.Binary(string="Image 10", store=True, )
    img11 = fields.Binary(string="Image 11", store=True, )
    img12 = fields.Binary(string="Image 12", store=True, )
    img13 = fields.Binary(string="Image 13", store=True, )
    img14 = fields.Binary(string="Image 14", store=True, )
    img15 = fields.Binary(string="Image 15", store=True, )
    img16 = fields.Binary(string="Image 16", store=True, )
    img17 = fields.Binary(string="Image 17", store=True, )
    img18 = fields.Binary(string="Image 18", store=True, )
    img19 = fields.Binary(string="Image 19", store=True, )
    img20 = fields.Binary(string="Image 20", store=True, )
    img21 = fields.Binary(string="Image 21", store=True, )
    img22 = fields.Binary(string="Image 22", store=True, )
    img23 = fields.Binary(string="Image 23", store=True, )
    img24 = fields.Binary(string="Image 24", store=True, )
    img25 = fields.Binary(string="Image 25", store=True, )
    img26 = fields.Binary(string="Image 26", store=True, )
    img27 = fields.Binary(string="Image 27", store=True, )
    img28 = fields.Binary(string="Image 28", store=True, )
    img29 = fields.Binary(string="Image 29", store=True, )
    img30 = fields.Binary(string="Image 30", store=True, )
    img31 = fields.Binary(string="Image 31", store=True, )
    img32 = fields.Binary(string="Image 32", store=True, )
    img33 = fields.Binary(string="Image 33", store=True, )
    img34 = fields.Binary(string="Image 34", store=True, )
    img35 = fields.Binary(string="Image 35", store=True, )
    img36 = fields.Binary(string="Image 36", store=True, )
    img37 = fields.Binary(string="Image 37", store=True, )
    img38 = fields.Binary(string="Image 38", store=True, )
    img39 = fields.Binary(string="Image 39", store=True, )
    img40 = fields.Binary(string="Image 40", store=True, )
    img41 = fields.Binary(string="Image 41", store=True, )
    img42 = fields.Binary(string="Image 42", store=True, )
    img43 = fields.Binary(string="Image 43", store=True, )
    img44 = fields.Binary(string="Image 44", store=True, )
    img45 = fields.Binary(string="Image 45", store=True, )
    img46 = fields.Binary(string="Image 46", store=True, )
    img47 = fields.Binary(string="Image 47", store=True, )
    img48 = fields.Binary(string="Image 48", store=True, )
    img49 = fields.Binary(string="Image 49", store=True, )
    img50 = fields.Binary(string="Image 50", store=True, )
    img51 = fields.Binary(string="Image 51", store=True, )
    img52 = fields.Binary(string="Image 52", store=True, )
    img53 = fields.Binary(string="Image 53", store=True, )
    img54 = fields.Binary(string="Image 54", store=True, )
    img55 = fields.Binary(string="Image 55", store=True, )
    img56 = fields.Binary(string="Image 56", store=True, )
    img57 = fields.Binary(string="Image 57", store=True, )
    img58 = fields.Binary(string="Image 58", store=True, )
    img59 = fields.Binary(string="Image 59", store=True, )
    img60 = fields.Binary(string="Image 60", store=True, )
    img61 = fields.Binary(string="Image 61", store=True, )
    img62 = fields.Binary(string="Image 62", store=True, )
    img63 = fields.Binary(string="Image 63", store=True, )
    img64 = fields.Binary(string="Image 64", store=True, )
    img65 = fields.Binary(string="Image 65", store=True, )
    img66 = fields.Binary(string="Image 66", store=True, )
    img67 = fields.Binary(string="Image 67", store=True, )
    img68 = fields.Binary(string="Image 68", store=True, )
    img69 = fields.Binary(string="Image 69", store=True, )
    img70 = fields.Binary(string="Image 70", store=True, )
    img71 = fields.Binary(string="Image 71", store=True, )
    img72 = fields.Binary(string="Image 72", store=True, )
    img73 = fields.Binary(string="Image 73", store=True, )
    img74 = fields.Binary(string="Image 74", store=True, )
    img75 = fields.Binary(string="Image 75", store=True, )
    img76 = fields.Binary(string="Image 76", store=True, )
    img77 = fields.Binary(string="Image 77", store=True, )
    img78 = fields.Binary(string="Image 78", store=True, )
    img79 = fields.Binary(string="Image 79", store=True, )
    img80 = fields.Binary(string="Image 80", store=True, )
    img81 = fields.Binary(string="Image 81", store=True, )
    img82 = fields.Binary(string="Image 82", store=True, )
    img83 = fields.Binary(string="Image 83", store=True, )
    img84 = fields.Binary(string="Image 84", store=True, )
    img85 = fields.Binary(string="Image 85", store=True, )
    img86 = fields.Binary(string="Image 86", store=True, )
    img87 = fields.Binary(string="Image 87", store=True, )
    img88 = fields.Binary(string="Image 88", store=True, )
    img89 = fields.Binary(string="Image 89", store=True, )
    img90 = fields.Binary(string="Image 90", store=True, )
    img91 = fields.Binary(string="Image 91", store=True, )
    img92 = fields.Binary(string="Image 92", store=True, )
    img93 = fields.Binary(string="Image 93", store=True, )
    img94 = fields.Binary(string="Image 94", store=True, )
    img95 = fields.Binary(string="Image 95", store=True, )
    img96 = fields.Binary(string="Image 96", store=True, )
    img97 = fields.Binary(string="Image 97", store=True, )
    img98 = fields.Binary(string="Image 98", store=True, )
    img99 = fields.Binary(string="Image 99", store=True, )
    img100 = fields.Binary(string="Image 100", store=True, )
    # Check boxes #
    is_img1 = fields.Boolean(string="Is Image1", store=True, )
    is_img2 = fields.Boolean(string="Is Image2", store=True, )
    is_img3 = fields.Boolean(string="Is Image3", store=True, )
    is_img4 = fields.Boolean(string="Is Image4", store=True, )
    is_img5 = fields.Boolean(string="Is Image5", store=True, )
    is_img6 = fields.Boolean(string="Is Image 6", store=True, )
    is_img7 = fields.Boolean(string="Is Image 7", store=True, )
    is_img8 = fields.Boolean(string="Is Image 8", store=True, )
    is_img9 = fields.Boolean(string="Is Image 9", store=True, )
    is_img10 = fields.Boolean(string="Is Image 10", store=True, )
    is_img11 = fields.Boolean(string="Is Image 11", store=True, )
    is_img12 = fields.Boolean(string="Is Image 12", store=True, )
    is_img13 = fields.Boolean(string="Is Image 13", store=True, )
    is_img14 = fields.Boolean(string="Is Image 14", store=True, )
    is_img15 = fields.Boolean(string="Is Image 15", store=True, )
    is_img16 = fields.Boolean(string="Is Image 16", store=True, )
    is_img17 = fields.Boolean(string="Is Image 17", store=True, )
    is_img18 = fields.Boolean(string="Is Image 18", store=True, )
    is_img19 = fields.Boolean(string="Is Image 19", store=True, )
    is_img20 = fields.Boolean(string="Is Image 20", store=True, )
    is_img21 = fields.Boolean(string="Is Image 21", store=True, )
    is_img22 = fields.Boolean(string="Is Image 22", store=True, )
    is_img23 = fields.Boolean(string="Is Image 23", store=True, )
    is_img24 = fields.Boolean(string="Is Image 24", store=True, )
    is_img25 = fields.Boolean(string="Is Image 25", store=True, )
    is_img26 = fields.Boolean(string="Is Image 26", store=True, )
    is_img27 = fields.Boolean(string="Is Image 27", store=True, )
    is_img28 = fields.Boolean(string="Is Image 28", store=True, )
    is_img29 = fields.Boolean(string="Is Image 29", store=True, )
    is_img30 = fields.Boolean(string="Is Image 30", store=True, )
    is_img31 = fields.Boolean(string="Is Image 31", store=True, )
    is_img32 = fields.Boolean(string="Is Image 32", store=True, )
    is_img33 = fields.Boolean(string="Is Image 33", store=True, )
    is_img34 = fields.Boolean(string="Is Image 34", store=True, )
    is_img35 = fields.Boolean(string="Is Image 35", store=True, )
    is_img36 = fields.Boolean(string="Is Image 36", store=True, )
    is_img37 = fields.Boolean(string="Is Image 37", store=True, )
    is_img38 = fields.Boolean(string="Is Image 38", store=True, )
    is_img39 = fields.Boolean(string="Is Image 39", store=True, )
    is_img40 = fields.Boolean(string="Is Image 40", store=True, )
    is_img41 = fields.Boolean(string="Is Image 41", store=True, )
    is_img42 = fields.Boolean(string="Is Image 42", store=True, )
    is_img43 = fields.Boolean(string="Is Image 43", store=True, )
    is_img44 = fields.Boolean(string="Is Image 44", store=True, )
    is_img45 = fields.Boolean(string="Is Image 45", store=True, )
    is_img46 = fields.Boolean(string="Is Image 46", store=True, )
    is_img47 = fields.Boolean(string="Is Image 47", store=True, )
    is_img48 = fields.Boolean(string="Is Image 48", store=True, )
    is_img49 = fields.Boolean(string="Is Image 49", store=True, )
    is_img50 = fields.Boolean(string="Is Image 50", store=True, )
    is_img51 = fields.Boolean(string="Is Image 51", store=True, )
    is_img52 = fields.Boolean(string="Is Image 52", store=True, )
    is_img53 = fields.Boolean(string="Is Image 53", store=True, )
    is_img54 = fields.Boolean(string="Is Image 54", store=True, )
    is_img55 = fields.Boolean(string="Is Image 55", store=True, )
    is_img56 = fields.Boolean(string="Is Image 56", store=True, )
    is_img57 = fields.Boolean(string="Is Image 57", store=True, )
    is_img58 = fields.Boolean(string="Is Image 58", store=True, )
    is_img59 = fields.Boolean(string="Is Image 59", store=True, )
    is_img60 = fields.Boolean(string="Is Image 60", store=True, )
    is_img61 = fields.Boolean(string="Is Image 61", store=True, )
    is_img62 = fields.Boolean(string="Is Image 62", store=True, )
    is_img63 = fields.Boolean(string="Is Image 63", store=True, )
    is_img64 = fields.Boolean(string="Is Image 64", store=True, )
    is_img65 = fields.Boolean(string="Is Image 65", store=True, )
    is_img66 = fields.Boolean(string="Is Image 66", store=True, )
    is_img67 = fields.Boolean(string="Is Image 67", store=True, )
    is_img68 = fields.Boolean(string="Is Image 68", store=True, )
    is_img69 = fields.Boolean(string="Is Image 69", store=True, )
    is_img70 = fields.Boolean(string="Is Image 70", store=True, )
    is_img71 = fields.Boolean(string="Is Image 71", store=True, )
    is_img72 = fields.Boolean(string="Is Image 72", store=True, )
    is_img73 = fields.Boolean(string="Is Image 73", store=True, )
    is_img74 = fields.Boolean(string="Is Image 74", store=True, )
    is_img75 = fields.Boolean(string="Is Image 75", store=True, )
    is_img76 = fields.Boolean(string="Is Image 76", store=True, )
    is_img77 = fields.Boolean(string="Is Image 77", store=True, )
    is_img78 = fields.Boolean(string="Is Image 78", store=True, )
    is_img79 = fields.Boolean(string="Is Image 79", store=True, )
    is_img80 = fields.Boolean(string="Is Image 80", store=True, )
    is_img81 = fields.Boolean(string="Is Image 81", store=True, )
    is_img82 = fields.Boolean(string="Is Image 82", store=True, )
    is_img83 = fields.Boolean(string="Is Image 83", store=True, )
    is_img84 = fields.Boolean(string="Is Image 84", store=True, )
    is_img85 = fields.Boolean(string="Is Image 85", store=True, )
    is_img86 = fields.Boolean(string="Is Image 86", store=True, )
    is_img87 = fields.Boolean(string="Is Image 87", store=True, )
    is_img88 = fields.Boolean(string="Is Image 88", store=True, )
    is_img89 = fields.Boolean(string="Is Image 89", store=True, )
    is_img90 = fields.Boolean(string="Is Image 90", store=True, )
    is_img91 = fields.Boolean(string="Is Image 91", store=True, )
    is_img92 = fields.Boolean(string="Is Image 92", store=True, )
    is_img93 = fields.Boolean(string="Is Image 93", store=True, )
    is_img94 = fields.Boolean(string="Is Image 94", store=True, )
    is_img95 = fields.Boolean(string="Is Image 95", store=True, )
    is_img96 = fields.Boolean(string="Is Image 96", store=True, )
    is_img97 = fields.Boolean(string="Is Image 97", store=True, )
    is_img98 = fields.Boolean(string="Is Image 98", store=True, )
    is_img99 = fields.Boolean(string="Is Image 99", store=True, )
    is_img100 = fields.Boolean(string="Is Image 100", store=True, )

    doctor_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])
    patient_id = fields.Many2one('res.partner', string='Patient Name')
    operator = fields.Char(string="Operator")
    referred_by = fields.Many2many('res.partner.category', string="Referred By", related="patient_id.category_id",
                                   readonly=True)
    id_patient = fields.Char(string="ID")
    # age = fields.Integer(string="Age", related="patient_id.member_age")
    # birth_date = fields.Date(string="Date of Birth", related="patient_id.birth_date")
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
    indications = fields.Text(string="Indication For Examination")
    procedures = fields.Char(string="Procedures")
    medications = fields.Char(string="Medications")
    findings = fields.Text(string="Findings")
    conclusions = fields.Text(string="Conclusions")
    recommendations = fields.Text(string="Recommendations")
    nurse = fields.Char(string="Nurse")
    nurse_assistant = fields.Char(string="Nursing assistant")
    patient_phone = fields.Char(string="Patient Phone", related="patient_id.phone", readonly=True)

    sale_order_id = fields.Many2one('sale.order', string="Sale Order")

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
