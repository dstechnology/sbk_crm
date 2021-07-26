from frappe import _

def get_data():
	return [
		{
			"label": _("Communication"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Interaction",
					"description": _("Details of Interaction customers."),
				},
				{
					"type": "doctype",
					"name": "Interaction Type",
					"description": _("Text Type of Interaction customers."),
				},
				{
					"type": "doctype",
					"name": "Interaction Result",
					"description": _("Status of Interaction"),
				},
				
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Interaction Details",
					"doctype": "Interaction Details"
				},
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "ToDo Details",
					"doctype": "ToDo Details"
				},
			]
		},
	]