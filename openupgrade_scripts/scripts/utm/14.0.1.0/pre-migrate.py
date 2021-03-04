# Copyright 2020 Odoo Community Association (OCA)
# Copyright (C) 2021 - Teclib'ERP (<https://www.teclib-erp.com>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from openupgradelib import openupgrade

_logger = logging.getLogger(__name__)


@openupgrade.migrate(use_env=False)
def migrate(cr, version):

    """
    Fix integrity error:
    update or delete on table "utm_stage" violates foreign key constraint
    "mail_mass_mailing_campaign_stage_id_fkey" on table "mail_mass_mailing_campaign"
    """

    campaign_stage_xmlid_renames = [
        (
            "utm.campaign_stage_1",
            "openupgrade_legacy_utm.campaign_stage_1",
        ),
        (
            "utm.campaign_stage_2",
            "openupgrade_legacy_utm.campaign_stage_2",
        ),
        (
            "utm.campaign_stage_3",
            "openupgrade_legacy_utm.campaign_stage_3",
        ),
    ]

    openupgrade.rename_xmlids(cr, campaign_stage_xmlid_renames, allow_merge=True)

