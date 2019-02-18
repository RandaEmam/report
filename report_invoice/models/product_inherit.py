from odoo import models,fields,api
from datetime import datetime

from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class product_inherit(models.Model):

    _inherit = 'product.template'

    exp_date = fields.Date('Expiration Date')


class sale_order(models.Model):
    _inherit = "sale.order"

    period_quo = fields.Integer("Days")




