###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, models
from odoo.http import request


class Website(models.Model):
    _inherit = "website"

    def recently_viewed_products(self):
        return request.env["website.sale.product.view"].search(
            [("session_id", "=", request.session.sid)], limit=6
        )

    def get_product_variant(self, viewed_product):
        combination_info = viewed_product.product_id._get_combination_info()
        return viewed_product.product_id.env["product.product"].browse(
            combination_info["product_id"]
        )
