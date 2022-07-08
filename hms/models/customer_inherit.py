from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class Customerinherit(models.Model):
    _inherit = 'res.partner'
    website = fields.Char()

    @api.constrains('email')
    def email_check(self):
        emailexist = self.env['hms.patient'].search(
            [('email', '=', self.email)])

        if emailexist:
            raise ValidationError("you cannot set that email")

    def unlink(self):
        if self.related_patient_id:
            raise ValidationError("Customer cannot be deleted")
        return super(Customerinherit, self).unlink()
