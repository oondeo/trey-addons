##############################################################################
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
##############################################################################
{
    "name": "Stock picking modify qty done wizard",
    "summary": "Wizard to modify qty done from a picking",
    "author": "Trey (www.trey.es)",
    "website": "https://www.trey.es",
    "license": "AGPL-3",
    "category": "Inventory",
    "version": "13.0.1.0.0",
    "depends": [
        "stock",
    ],
    "data": [
        "wizards/stock_picking_modify_qty_done.xml",
        "views/stock_picking_views.xml",
    ],
}
