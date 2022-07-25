###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PrintOptionsStockPicking(models.TransientModel):
    _name = "print.options.stock.picking"
    _description = "Prints according to options selected."

    name = fields.Char(
        string="Empty",
    )

    def button_print(self):
        raise ValidationError(
            _(
                "You must define options fields for this wizard and report to "
                "return."
            )
        )
