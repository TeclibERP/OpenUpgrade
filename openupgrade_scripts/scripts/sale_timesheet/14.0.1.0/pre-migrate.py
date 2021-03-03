# Copyright 2020 Odoo Community Association (OCA)
# Copyright (C) 2021 - Teclib'ERP (<https://www.teclib-erp.com>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import logging

from openupgradelib import openupgrade
from odoo import tools

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=False)
def migrate(cr, version):

    # Fix error on views update
    cr.execute(
        """ DELETE FROM ir_ui_view WHERE model = 'project.task'
        AND name in (
        'project.task.form.inherit.sale.line.editable.salesman',
        'sale.service.form.view.inherit',
        'project.task.form.inherit.timesheet',
        'view.task.form2.inherit');
    """
    )
