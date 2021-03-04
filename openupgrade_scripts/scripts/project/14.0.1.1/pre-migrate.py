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
    Fix error on deleting ir.model.fields.selection (project.selection__project_project__rating_status__no)
    """
    cr.execute(
        """ UPDATE  project_project SET rating_status='' ;
    """
    )

