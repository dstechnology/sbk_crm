// Copyright (c) 2016, DPI and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Interaction Detail"] = {
	"filters": [
        {
            "fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), -14)
        },
        {
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_days(frappe.datetime.get_today(), 16)
		},
		{
			"fieldname": "result",
			"label": __("Results"),
			"fieldtype": "Check"
		}
		
    ]
}
