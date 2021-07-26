# Copyright (c) 2013, DPI and contributors
# For license information, please see license.txt

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
	query="""Select priority, date, description, owner, reference_type, reference_name,assigned_by  
	    from `tabToDo` where (date between '{0}' 
		and '{1}')""".format(filters.get("from_date"),filters.get("to_date"))

	
	
	dl = frappe.db.sql(query,as_list=1,debug=1)
	return dl

def  get_colums():
	columns = ["Priority:Data:100"]+["Date:Date:100"]+["Description:Data:100"]+["Allocated To:Data:100"]\
	+["Reference Type:Data:140"]+["Reference Name:100"]\
	+["Assigned By:Data:140"]
	return columns
