###############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2021-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
###############################################################################
{
    "name": "Product standard price history team",
    "summary": "Add team how markets in standard price history",
    "category": "CRM",
    "version": "13.0.1.0.0",
    "author": "Trey (www.trey.es)",
    "website": "https://www.trey.es",
    "license": "AGPL-3",
    "depends": [
        "delivery",
        "product_standard_price_history",
        "sales_team",
    ],
    "data": [
        "views/crm_team_views.xml",
        "views/product_standard_price_history.xml",
    ],
}
