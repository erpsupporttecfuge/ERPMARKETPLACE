from odoo import models,fields,api,_

class ResPartnerCustom(models.Model):
    _inherit = 'res.partner'


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            company = self.env['res.company'].browse(vals.get('company_id')) or self.env.company
            vals['company_id'] = company.id
        return super().create(vals_list)