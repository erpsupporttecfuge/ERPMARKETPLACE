from odoo import models,fields,api,_
import random
import string

class ResCompany(models.Model):
    _inherit = 'res.company'

    password = fields.Char(string="Password")
    state=fields.Selection([
        ('draft','Draft'),
        ('done','Done'),
    ],default='draft')

    @api.onchange('email')
    def generate_password(self):
        characterList = string.ascii_letters + string.digits + string.punctuation
        self.password = ''.join(random.sample(characterList, 8))

    def create_user(self):
        self.state = 'done'
        template = self.env.ref('market_place_customisation.user_password_for_user_company_mail_template')
        user_values = {
            'name': self.name,
            'login':self.email,
            'password':self.password,
            'phone':self.phone,
            'company_ids':self.ids,
            'company_id':self.id,
        }
        user = self.env['res.users'].create(user_values)
        group_id = self.env.ref('market_place_customisation.product_edit_group_user')
        group_id.users = [(4, user.id)]
        template.send_mail(self.id, force_send=True)
        return user