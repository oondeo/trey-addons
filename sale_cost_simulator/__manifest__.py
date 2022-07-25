##############################################################################
#
#    Trey, Kilobytes de Soluciones
#    Copyright (C) 2017-Today Trey, Kilobytes de Soluciones <www.trey.es>
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
    "name": "Sale cost simulator",
    "summary": "Sale cost simulator",
    "description": "Sale cost simulator",
    "author": "Trey (www.trey.es)",
    "website": "https://www.trey.es",
    "license": "AGPL-3",
    "category": "Sale",
    "version": "13.0.1.0.0",
    "depends": [
        "mail",
        "print_formats_base",
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/multicompany.xml",
        "data/ir_actions_server.xml",
        "data/sale_cost_simulator_templates.xml",
        "wizards/import_line.xml",
        "wizards/apply_pricelist.xml",
        "views/sale_cost_line_views.xml",
        "views/sale_cost_simulator_views.xml",
        "views/menus.xml",
        "reports/report_sale_cost_simulation.xml",
    ],
    "installable": True,
}
