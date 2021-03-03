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
    Fix error on mail_mass_mailing_list_rel
    #ERROR: odoo.sql_db: bad query:
            ALTER TABLE "mail_mass_mailing_list_rel"
            ADD FOREIGN KEY ("mailing_mailing_id")
            REFERENCES "mailing_mailing"("id") ON DELETE cascade
    #ERROR: column "mailing_mailing_id" referenced in foreign key constraint does not exist
    """
    cr.execute(
        """ ALTER TABLE mail_mass_mailing_list_rel
    RENAME mail_mass_mailing_id TO mailing_mailing_id;
    ALTER TABLE public.mail_mass_mailing_list_rel
    RENAME mail_mass_mailing_list_id TO mailing_list_id;
    """
    )
