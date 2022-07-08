from odoo import models ,fields,api
import re
from odoo.odoo.exceptions import ValidationError, UserError
from datetime import date

class patient(models.Model):
    _name = "hms.patient"

    fname = fields.Char(required=True)
    lname = fields.Char(required=True)
    age = fields.Integer()
    Birthday = fields.Date()
    image = fields.Image()
    address = fields.Text()
    department_id = fields.Many2one('hms.department')
    department_capacity = fields.Integer(related='department_id.capacity')
    doctors_id = fields.Many2many('hms.doctors')
    history = fields.Html()
    cr_ratio = fields.Float()
    state = fields.Selection([
        ('un', 'Undetermind'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')])
    blood = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ])
    pcr = fields.Boolean()
    log_ids = fields.One2many('hms.patientLog', 'patient_id')

    @api.onchange('age')
    def _onchange_age(self):
        if self.age < 30:
            self.pcr = True
        return {
            'warning': {
                'title': "Something bad happened",
                'message': "It was very bad indeed",
            }
        }

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'Good':
            return "State changed to 'Good'. "
        elif self.state == 'Fair':
                return "State changed to 'Fair'. "
        elif self.state == 'Serious':
            return "State changed to 'Serious'. "
        else:
            return "Undetermind"





