##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2019-Today Trey, Kilobytes de Soluciones <www.trey.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Account intercompany",
    "summary": "Check and prepare account for create intercompany invoices",
    "author": "Trey (www.trey.es)",
    "website": "https://www.trey.es",
    "license": "AGPL-3",
    "category": "Sales",
    "version": "13.0.1.0.0",
    "depends": [
        "account",
        "account_payment_partner",
    ],
    "data": [
        "security/ir_rule.xml",
        "security/res_groups.xml",
        "views/account_account.xml",
        "views/account_journal.xml",
        "views/account_payment_mode.xml",
        "views/account_payment_term.xml",
        "views/account_tax.xml",
    ],
}
