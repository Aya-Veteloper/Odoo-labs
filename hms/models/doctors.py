from odoo import models ,fields,api

class Doctors(models.Model):
    _name = "hms.doctors"

    fname = fields.Char(required=True)
    lname = fields.Char(required=True)
    image = fields.Image()
    patient_id = fields.Many2many('hms.patient', 'doctors_id')

