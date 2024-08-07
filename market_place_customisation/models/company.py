from odoo import models,fields,api,_


class ResCompany(models.Model):
    _inherit = 'res.company'

    state=fields.Selection([
        ('draft','Draft'),
        ('done','Done'),
    ],default='draft')

    def create_user(self):
        self.state = 'done'
        user_values = {
            'name': self.name,
            'login':self.email,
            'phone':self.phone,
            'company_ids':self.ids,
            'company_id':self.id,
        }
        user = self.env['res.users'].create(user_values)
        group_id = self.env.ref('market_place_customisation.product_edit_group_user')
        group_id.users = [(4, user.id)]
        return user