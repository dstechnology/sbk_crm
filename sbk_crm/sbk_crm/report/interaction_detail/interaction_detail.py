from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt, cint
import erpnext

def execute(filters=None):
	validate_filters(filters)
	message=''
	data = []
	columns = get_colums()
	chart = get_chart_data(filters)
	data = get_data(filters)
	return columns, data, message, chart
def validate_filters(filters):
	if filters.from_date > filters.to_date:
		frappe.throw(_("From Date must be before To Date"))

def get_data(filters):
	query="""Select date, reference_name,responsible, type_of_call, type_of_interaction, person_interacted_with, result,
	    	remarks, next_action_by, next_action_date, next_action_task, reference_doctype, customer, lead, supplier  
	    	from `tabInteraction`where (date between '{0}' 
			and '{1}')""".format(filters.get("from_date"),filters.get("to_date"))

	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl

def  get_colums():

	columns = ["Date:Date:80"]+["Reference Name:Dynamic Link/Reference Doctype:80"]+["Responsible:Data:80"]\
		+["Type of call:Data:100"]+["Type of Interaction:Data:100"]+["Person Interacted with:Data:80"]\
		+["Result:Data:100"]+["Remarks:Data:140"]+["Next Action By:Data:100"]\
		+["Next Action Date:Date:100"]+["Next Action Task:Data:100"]+["Reference Doctype:Data:140"]\
		+["Customer:Link/Customer:140"]+["Lead:Link/Lead:140"]+["Supplier:Link/Supplier:100"]

	return columns
def get_chart_data(filters):
	labels = []
	values = []
	if filters.get("result"):
		data_for_chart= frappe.db.sql("""select count(name) as count_of_result,result 
			from tabInteraction 
			where (date between '{0}' 
				and '{1}')
			group by result order by count_of_result desc""".format(filters.get("from_date"),filters.get("to_date")),as_dict=1)	
		
		for i in data_for_chart:
			labels.append(i.result)
			values.append(i.count_of_result)
	else :
		data_for_chart= frappe.db.sql("""select count(name) as count_of_type_of_interaction,type_of_interaction 
			from tabInteraction 
			where (date between '{0}' 
				and '{1}')
			group by type_of_interaction order by count_of_type_of_interaction desc""".format(filters.get("from_date"),filters.get("to_date")),as_dict=1)	

		for i in data_for_chart:
			labels.append(i.type_of_interaction)
			values.append(i.count_of_type_of_interaction)
	datasets = [
		{
			'label': labels,
			'values': values
			}	
		]
	chart = {
		"data": {
			'labels': labels,
			'datasets': datasets
		}
	}
	chart["type"] = "bar"
	return chart

