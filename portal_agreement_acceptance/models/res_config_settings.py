###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    limit_agreements = fields.Integer(
        string="Maximum number of agreements to show",
        related="website_id.limit_agreements",
        readonly=False,
    )

    @api.model
    def get_values(self):
        res = super().get_values()
        config_parameter = self.env["ir.config_parameter"].sudo()
        limit = int(config_parameter.get_param("website.limit_agreements"))
        res.update(limit_agreements=limit)
        return res

    def set_values(self):
        super().set_values()
        set_param = self.env["ir.config_parameter"].sudo().set_param
        set_param("website.limit_agreements", self.limit_agreements)
