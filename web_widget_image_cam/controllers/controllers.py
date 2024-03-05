from odoo import http
from odoo.http import request, route


class MedicalEndoscopesController(http.Controller):

    @route('/medical_endoscopes/save_video', type='json', auth='user')
    def save_video(self, recorded_data):
        medical_endoscopes_model = request.env['medical.endoscopes']
        medical_endoscopes_model._save_video(recorded_data)
        print("@@@@@@@@@@@@@@@@@")
        return {'success': True}
