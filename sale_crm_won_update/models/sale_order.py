# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order'


    crm_won_stage = fields.Boolean(string='Won Opportunity', default=False, compute='_compute_crm_won_stage')

    @api.depends('opportunity_id')
    def _compute_crm_won_stage(self):
        for order in self:
            if order.opportunity_id:
                order.crm_won_stage = order.opportunity_id.stage_id.is_won
            else:
                order.crm_won_stage = True

    def crm_won_update(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Update Opportunity to Won Stage?'),
            'res_model': 'wizard.sale.crm.won.update',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
                'default_crm_id': self.opportunity_id.id,
            }
        }

    def action_update_opportunity_won(self):
        self.opportunity_id.action_set_won_rainbowman()
        self.opportunity_id.message_post(
            subject='Quotation Confirmed',
            body='Quotation Confirmed: %s' % self.name,
            message_type='notification',
            subtype_xmlid='mail.mt_note'
        )
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Opportunity Updated',
                'type': 'success',
                'message': 'Opportunity updated to Won stage',
                'sticky': False,
                'next': {
                    'type': 'ir.actions.client',
                    'tag': 'reload',
                }
            }
        }