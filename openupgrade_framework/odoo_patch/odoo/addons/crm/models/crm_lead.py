# Copyright Odoo Community Association (OCA)
# Copyright (C) 2021 - Teclib'ERP (<https://www.teclib-erp.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade
from odoo.addons.crm.models.crm_lead import Lead


def _phone_get_number_fields(self):
    """ This method returns the fields of phone number to validate """
    return ['phone']


Lead._phone_get_number_fields = _phone_get_number_fields
