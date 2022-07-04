from odoo import models, fields, api


class InvoicingReportModule(models.Model):
    _inherit = 'account.move'


class SaleOrderReportSignatures(models.Model):
    _inherit = 'sale.order'


class PurchaseOrderReportSignatures(models.Model):
    _inherit = 'purchase.order'


class DeliverySlipReportSignatures(models.Model):
    _inherit = 'stock.picking'
