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
    "name": "Product supplierinfo for customer copy",
    "summary": "Wizard to copy information about a product customer info for "
    "to other partner",
    "category": "Sales Management",
    "version": "13.0.1.0.0",
    "author": "Trey (www.trey.es)",
    "website": "https://www.trey.es",
    "license": "AGPL-3",
    "depends": [
        "product",
        "product_supplierinfo_for_customer",
        "product_supplierinfo_for_customer_menu",
        "sale_management",
    ],
    "data": [
        "wizards/product_supplierinfo_for_customer_copy.xml",
    ],
}
