# Copyright 2018 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import re

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    multiple_discount = fields.Char(
        string="Disc. Applied",
    )
    discount_name = fields.Char()

    @staticmethod
    def _validate_discount(discount):
        discount_regex = re.compile(
            r"^(\s*[-+]{0,1}\s*\d+([,.]\d+)?){1}"
            r"(\s*[-+]\s*\d+([,.]\d+)?\s*)*$"
        )

        # This regex is composed of 2 parts:
        # 1) A starting number which is mandatory {1} composed of:
        #    a) \s* = any number of starting spaces
        #    b) [-+]{0,1} = an optional symbol '+' or '-'
        #    c) \s* = any number of spaces
        #    d) \d+ = a digit sequence of length at least 1
        #    e) ([,.]\d+)? = an optional decimal part, composed of a '.' or ','
        #       symbol followed by a digital sequence of length at least 1
        # 2) An optional list of other numbers each one composed of:
        #    a) \s* = any number of starting spaces
        #    b) [-+] = a mandatory '+' or '-' symbol
        #    c) \s* = any number of spaces
        #    d) \d+ = a digit sequence of length at least 1
        #    e) ([,.]\d+)? = an optional decimal part, composed of a '.' or ','
        #       symbol followed by a digital sequence of length at least 1
        #    f) \s* = any number of ending spaces

        if discount and not discount_regex.match(discount):
            return False
        return True

    @api.onchange("multiple_discount")
    def onchange_multiple_discount(self):
        def _normalize_discount(discount):
            discount = discount.replace(" ", "")
            discount = discount.replace(",", ".")
            if discount and discount[0] == "+":
                discount = discount[1:]
            return discount

        for line in self:
            if line.multiple_discount:
                if self._validate_discount(line.multiple_discount):
                    normalized_discount = _normalize_discount(
                        line.multiple_discount
                    )
                else:
                    line.discount = 0
                    raise UserError(
                        _("Warning! The discount format is not recognized.")
                    )

                tokens = re.split(r"([+-])", normalized_discount)
                numeric_tokens = []
                last_sign = 1
                for token in tokens:
                    if not token:
                        continue
                    if token == "-":
                        last_sign = -1
                    elif token == "+":
                        last_sign = 1
                    else:
                        numeric_tokens.append(float(token) * last_sign)
                marginal_discount = 1
                for token in numeric_tokens:
                    marginal_discount = marginal_discount * (1 - (token / 100))
                total_discount = 1 - marginal_discount
                line.discount = total_discount * 100
                if normalized_discount != line.multiple_discount:
                    line.multiple_discount = normalized_discount
            else:
                line.discount = 0

    @api.constrains("multiple_discount")
    def validate_discount(self):
        for line in self:
            if line.multiple_discount and not self._validate_discount(
                line.multiple_discount
            ):
                raise ValidationError(
                    _("Warning! The discount format is not recognized.")
                )

    def write(self, vals):
        res = super().write(vals)
        if "multiple_discount" in vals:
            for line in self:
                line.onchange_multiple_discount()
        return res

    @api.onchange("product_id")
    def _onchange_product_id_multiple_discount(self):
        invoice_type = self.env.context.get("type", False)
        if not self.product_id:
            if invoice_type not in ("in_invoice", "in_refund"):
                self.price_unit = 0.0
            return {"uom_id": []}
        if invoice_type not in ("in_invoice", "in_refund"):
            rule = self.env["product.pricelist.item"]
            pricelist = self.partner_id.property_product_pricelist
            product_context = dict(
                self.env.context,
                partner_id=self.invoice_id.partner_id.id,
                date=self.invoice_id.date_invoice,
                uom=self.uom_id.id,
            )
            final_price, rule_id = pricelist.with_context(
                product_context
            ).get_product_price_rule(
                self.product_id,
                self.quantity or 1.0,
                self.invoice_id.partner_id,
            )
            rules = rule.browse(rule_id)
            if rules.exists() and not rules.without_discount:
                self.multiple_discount = rules._get_item_discount()
                self.discount_name = rules._get_item_name()
