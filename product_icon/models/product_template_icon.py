###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ProductTemplateIcon(models.Model):
    _name = "product.template.icon"
    _description = "Product template icon"
    _rec_name = "sequence"

    sequence = fields.Integer(
        string="Sequence",
    )
    icon_id = fields.Many2one(
        comodel_name="product.icon",
        string="Icon",
        index=True,
        required=True,
    )
    product_template_id = fields.Many2one(
        comodel_name="product.template",
        string="Product template",
        index=True,
        required=True,
    )
    image = fields.Binary(
        related="icon_id.image_small",
    )
