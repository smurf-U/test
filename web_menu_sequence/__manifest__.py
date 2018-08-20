# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Menu Sequence',
    'category': 'web',
    'version': '11.0.1.0.0',
    'description':
        """
Odoo Web Menu Sequence.
========================

This module provides re-arrange menu sequence prior to user.
        """,
    'depends': ['web'],
    'data': [
        'view/preference.xml',
    ],
    'application': True,

}
