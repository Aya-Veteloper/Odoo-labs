from odoo import models, fields, api


class Department(models.Model):
    _name = "hms.department"

    name = fields.Char()
    patient_id = fields.One2many('hms.patient', 'department_id')
    capacity = fields.Integer()
    Is_opened = fields.Boolean()

