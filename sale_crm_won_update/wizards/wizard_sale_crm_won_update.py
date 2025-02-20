from odoo import models, fields, api

class WizardSaleCrmWonUpdate(models.TransientModel):
    _name = 'wizard.sale.crm.won.update'
    _description = 'Wizard Sale CRM Won Update'

    crm_id = fields.Many2one('crm.lead', string='Opportunity')
    stage_id = fields.Many2one('crm.stage', string='Current Stage', related='crm_id.stage_id')
    sale_order_id = fields.Many2one('sale.order', string='Sale Order')

    def action_confirm_auto(self):
        self.crm_id.action_set_won_rainbowman()
        self.crm_id.message_post(
            subject='Quotation Confirmed',
            body='Quotation Confirmed: %s' % self.sale_order_id.name,
            message_type='notification',
            subtype_xmlid='mail.mt_note'
        )
        self.sale_order_id.action_confirm()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Opportunity Updated',
                'type': 'success',
                'message': 'Opportunity updated to Won stage',
                'sticky': False,
                'next': {
                    'type': 'ir.actions.act_window_close',
                }
            }
        }

    def action_skip(self):
        self.sale_order_id.action_confirm()
        return False