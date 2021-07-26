from __future__ import unicode_literals
import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_colums()
	data = get_data(filters)
	validate_filters(filters)

	return columns, data

def validate_filters(filters):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))


def get_data(filters):
	query="""Select date, reference_name,responsible, type_of_call, type_of_interaction, person_interacted_with, result,
	    	remarks, next_action_by, next_action_date, next_action_task, reference_doctype, customer, lead, supplier  
	    	from `tabInteraction` where (date between '{0}' 
			and '{1}')""".format(filters.get("from_date"),filters.get("to_date"))

	
	
	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl

def  get_colums():

	columns = ["Date:Date:100"]+["Reference Name:Dynamic Link/Reference Doctype:180"]+["Responsible:Data:100"]\
		+["Type of call:Data:100"]+["Type of Interaction:Data:100"]+["Person Interacted with:Data:100"]\
		+["Result:Data:100"]+["Remarks:Data:140"]+["Next Action By:Data:100"]\
		+["Next Action Date:Date:100"]+["Next Action Task:Data:100"]+["Reference Doctype:Data:140"]\
		+["Customer:Link/Customer:140"]+["Lead:Link/Lead:140"]+["Supplier:Link/Supplier:100"]

	return columns
