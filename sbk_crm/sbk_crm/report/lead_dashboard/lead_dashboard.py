# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

#from _future_ import unicode_literals
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
		
def  get_colums():
	columns = ["Lead Id:Link/Lead:100"]+["Lead Name:Data:180"]+["Company Name:Data:100"]+["Status:Data:100"]+["Gender:Link/Gender:60"]\
		+["Source:Link/Lead Source:100"]+["Customer:Link/Customer:100"]+["Email Id:Data:140"]+["Source:Link/Lead Source:100"]+["Lead Owner:Link/User:100"]\
		+["Next Contact Date:Datetime:140"]+["Next Contact By:Link/User:100"]+["Phone:Data:100"]+["Salutation:Link/Salutation:100"]+["Mobile No:Data:100"]\
		+["Fax:Data:100"]+["Website:Data:100"]+["Territory:Link/Territory:100"]+["Lead Type:Select:100"]+["Industry:Link/Industry Type:100"]\
		+["Request Type:Select Type:100"]+["Market Segment:Select Type:100"]+["Company:Link/Company:100"]
	return columns

def get_data(filters):
	query="""Select name, lead_name, company_name, status, 
				gender, source, customer, email_id, source, 
				lead_owner, contact_date, contact_by,
				phone, salutation, mobile_no, fax, website,
				territory, type, industry, request_type, market_segment, company
	    	from `tabLead` 
			where creation between '{0}' and '{1}'""".format(filters.get("from_date"),filters.get("to_date"))
	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl


def get_chart_data(filters):

	data_for_chart= frappe.db.sql("""select count(name) as count_of_status,status 
		from tabLead 
		where creation between '{0}' and '{1}'
		group by status order by count_of_status desc""".format(filters.get("from_date"),filters.get("to_date")),as_dict=1)	

	labels = []
	values = []
	for i in data_for_chart:
		labels.append(i.status)
		values.append(i.count_of_status)

	

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


