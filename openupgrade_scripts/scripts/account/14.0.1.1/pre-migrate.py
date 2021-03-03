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
    Fix error on account_reconcile_model_analytic_tag_rel
        ERROR: odoo.sql_db: bad query:
            ALTER TABLE "account_reconcile_model_analytic_tag_rel"
            ADD FOREIGN KEY ("account_reconcile_model_line_id")
            REFERENCES "account_reconcile_model_line"("id") ON DELETE cascade
        ERROR: column "account_reconcile_model_line_id" referenced in foreign key constraint does not exist

    """
    cr.execute(
        """ ALTER TABLE account_reconcile_model_analytic_tag_rel
        RENAME account_reconcile_model_id TO account_reconcile_model_line_id;
    """
    )

    # Fix error on _process_ondelete
    cr.execute(
        """ DELETE FROM ir_model WHERE model='account.accrual.accounting.wizard';
    """
    )
