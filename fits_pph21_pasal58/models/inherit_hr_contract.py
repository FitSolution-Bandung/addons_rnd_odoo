from dateutil.relativedelta import relativedelta
from odoo import models, fields, api, _


class HRContract(models.Model):
    _inherit = 'hr.version'

    tunjangan_pajak = fields.Selection([('gross', 'Gross'), ('grossup', 'GrossUp')], string="Metode Pajak", default='gross')
