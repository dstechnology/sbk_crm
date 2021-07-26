# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sbk_crm"
app_title = "SBK CRM"
app_publisher = "DPI"
app_description = "Test"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "pgole21@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sbk_crm/css/sbk_crm.css"
# app_include_js = "/assets/sbk_crm/js/sbk_crm.js"

# include js, css files in header of web template
# web_include_css = "/assets/sbk_crm/css/sbk_crm.css"
# web_include_js = "/assets/sbk_crm/js/sbk_crm.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
fixtures = ["custom_field","Property Setter","Print Format"]
# Home Pages
# ----------
doctype_js = {
    "Lead":["custom_script/lead.js"],
    "Sales Order":["custom_script/sales_order.js"],
    "Quotation":["custom_script/quotation.js"],
    "Supplier":["custom_script/supplier.js"],
    "Sales Invoice":["custom_script/sales_invoice.js"],
    "Customer":["custom_script/customer.js"],
    "Delivery Note":["custom_script/delivery_note.js"],
    "Payment Entry":["custom_script/payment_entry.js"],
    "Journal Entry":["custom_script/journal_entry.js"],
    "Purchase Order":["custom_script/purchase_order.js"],
    "Purchase Invoice":["custom_script/purchase_invoice.js"],
    "Purchase Receipt":["custom_script/purchase_receipt.js"],
    "Request for Quotation":["custom_script/request_for_quotation.js"],
    "Material Request":["custom_script/material_request.js"],
    "Supplier Quotation":["custom_script/supplier_quotation.js"],

    "Brand":["custom_script/brand.js"]
}
# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sbk_crm.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sbk_crm.install.before_install"
# after_install = "sbk_crm.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sbk_crm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sbk_crm.tasks.all"
# 	],
# 	"daily": [
# 		"sbk_crm.tasks.daily"
# 	],
# 	"hourly": [
# 		"sbk_crm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sbk_crm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sbk_crm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sbk_crm.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sbk_crm.event.get_events"
# }

