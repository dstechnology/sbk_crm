# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import print_function, unicode_literals

import frappe
from frappe import _
from frappe.desk.page.setup_wizard.setup_wizard import add_all_roles_to
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

default_mail_footer = """<div style="padding: 7px; text-align: right; color: #888"><small>Sent via
	<a style="color: #888" href="http://sbknext.com">SBKNext</a></div>"""

def after_install():
	#frappe.get_doc({'doctype': "Role", "role_name": "Analytics"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Webex"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Skype"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "SMS"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Whatsaap"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Existing Customer Visit"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Follow Up Visit"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Cold Visit"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Mail"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Follow Up Call"}).insert()
	frappe.get_doc({'doctype': "Interaction Type", "type_of_interaction": "Cold Call"}).insert()


	frappe.get_doc({'doctype': "Interaction Result", "result": "Status Quo"}).insert()
	frappe.get_doc({'doctype': "Interaction Result", "result": "Closed Won"}).insert()
	frappe.get_doc({'doctype': "Interaction Result", "result": "Closed Lost"}).insert()
	frappe.get_doc({'doctype': "Interaction Result", "result": "Colder"}).insert()
	frappe.get_doc({'doctype': "Interaction Result", "result": "Warmer"}).insert()


	frappe.db.commit()

def ping():
	print("hii...,.;")