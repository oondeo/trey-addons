###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, api, models


class ImportTemplate(models.Model):
    _inherit = "import.template"
    _description = "Template for imports"

    @api.depends("model_id")
    def _compute_template_file_name(self):
        super()._compute_template_file_name()
        for template in self:
            if template.model_id.model == "import.template.pricelist.item":
                template.template_file_name = _("template_pricelist_item.xlsx")
