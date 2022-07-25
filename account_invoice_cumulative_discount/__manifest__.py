# Copyright 2018 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Account Invoice Cumulative Discount",
    "summary": "Express discounts on Invoice lines as mathematical "
    "expressions",
    "author": "Onestein, Trey (www.trey.es), Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/account-invoicing/",
    "category": "Accounting",
    "license": "AGPL-3",
    "version": "13.0.1.0.0",
    "depends": [
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/account_invoice_views.xml",
        "views/product_pricelist_views.xml",
        "reports/report_invoice.xml",
    ],
}
