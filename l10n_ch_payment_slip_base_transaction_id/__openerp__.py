# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2014 Camptocamp SA
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

{'name': 'Switzerland - BVR/ESR Transaction ID Compatibility',
 'version': '1.0',
 'author': "Camptocamp,Odoo Community Association (OCA)",
 'maintainer': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'Hidden',
 'depends': ['l10n_ch_payment_slip',
             'base_transaction_id'],
 'description': """
Swiss BVR/ESR Transaction ID Compatibility
==========================================

Link module between the Swiss localization BVR/ESR module
(l10n_ch_payment_slip) and the module adding a transaction ID
field (base_transaction_id).

When an invoice has a transaction ID, no BVR reference should be generated
because the reconciliation should be done with the transaction ID, not
a new reference.

This module is needed if you use the Swiss localization module and the
bank-statement-reconcile project in the banking addons
(https://launchpad.net/banking-addons).

 """,
 'website': 'http://www.camptocamp.com',
 'data': [],
 'tests': [],
 'installable': False,
 'auto_install': True,
 }
