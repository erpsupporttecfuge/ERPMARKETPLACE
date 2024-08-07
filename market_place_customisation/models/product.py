from odoo import fields,models,api,_

class ProductTemplateCustomisation(models.Model):
    _inherit='product.template'

    is_invisible = fields.Boolean(string="Un Invisible",store=True,default="True")
    is_group = fields.Boolean(related='is_invisible')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            company = self.env['res.company'].browse(vals.get('company_id')) or self.env.company
            vals['company_id'] = company.id
            vals['is_invisible'] = False
        return super().create(vals_list)