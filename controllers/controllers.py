# -*- coding: utf-8 -*-
# from odoo import http


# class SubscriptionExtended(http.Controller):
#     @http.route('/subscription_extended/subscription_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/subscription_extended/subscription_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('subscription_extended.listing', {
#             'root': '/subscription_extended/subscription_extended',
#             'objects': http.request.env['subscription_extended.subscription_extended'].search([]),
#         })

#     @http.route('/subscription_extended/subscription_extended/objects/<model("subscription_extended.subscription_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('subscription_extended.object', {
#             'object': obj
#         })
