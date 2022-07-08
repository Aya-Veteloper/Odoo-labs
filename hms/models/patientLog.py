from odoo import models , fields



class PatientLog(models.Model):

    _name = 'hms.patientLog'

    description = fields.Text()
    patient_id = fields.Many2one('hms.patient')