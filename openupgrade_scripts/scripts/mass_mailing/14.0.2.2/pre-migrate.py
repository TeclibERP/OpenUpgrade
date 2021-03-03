# Copyright 2020 Odoo Community Association (OCA)
# Copyright (C) 2021 - Teclib'ERP (<https://www.teclib-erp.com>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from openupgradelib import openupgrade

from odoo import tools

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=False)
def migrate(cr, version):
    """
    Fix error on mailing_contact_res_partner_category_rel
    #ERROR: odoo.sql_db: bad query:
            ALTER TABLE "mailing_contact_res_partner_category_rel"
            ADD FOREIGN KEY ("mailing_contact_id") REFERENCES "mailing_contact"("id") ON DELETE cascade
    #ERROR: column "mailing_contact_id" referenced in foreign key constraint does not exist
    """
    cr.execute(
        """ ALTER TABLE mailing_contact_res_partner_category_rel
    RENAME mail_mass_mailing_contact_id TO mailing_contact_id;
    """
    )
