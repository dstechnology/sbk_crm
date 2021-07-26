from __future__ import unicode_literals
import frappe, json
import frappe.desk.form.meta
import frappe.desk.form.load
import frappe.permissions
import json
from frappe.model.document import Document
from frappe import _
import math, random


@frappe.whitelist()
def ping():
	print("s")
	return 1


@frappe.whitelist(allow_guest=True)
def verify_otp(user,otp):
	print("s")
	verify = frappe.cache().get_value(f'{user}')
	print(verify)
	if verify==otp:
		frappe.cache().delete_key(f'{user}')
		return 'success'
	else:
		return 'failed'

@frappe.whitelist()
def generateOTP(user) :
	# function to generate OTP

	# Declare a digits variable 
	# which stores all digits
	digits = "0123456789"
	OTP = ""

	# if not frappe.db.get_value("New User", user):
	# 	return 'invalid'

	# length of password can be chaged
	# by changing value in range
	for i in range(4) :
		OTP += digits[math.floor(random.random() * 10)]

	frappe.cache().set_value(f'{user}', OTP, expires_in_sec=60)
	frappe.db.commit()
	return OTP


# @frappe.whitelist()
# def add_expense(exp_approver='',remark=''):
# 	print("hello")
# 	"""allow any logged user to post toDo via interaction master"""
# 	# doc = frappe.get_doc("Expense Claim")
# 	expense = frappe.new_doc("Expense Claim")
# 	print("in")
# 	# expense.approval_status = approval_status
# 	expense.exp_approver = exp_approver
# 	# expense.is_paid = is_paid
# 	expense.remark = remark
# 	expense.insert(ignore_permissions=True)
# 	expense.save(ignore_permissions=True)
# 	frappe.db.commit()
# 	frappe.msgprint("New Expense record created");
	# return {"message":"Claim added successfully"}
		

@frappe.whitelist()
def create_todo(owner, assigned_by, description, date,reference_name,reference_type):
		"""allow any logged user to post toDo via interaction master"""
		#emp = frappe.db.get_value("ToDo",{"owner":owner, "reference_name": reference_name},"owner")
		#if emp:
		todo = frappe.new_doc("ToDo")
		todo.owner = owner
		todo.assigned_by = assigned_by
		todo.description = description
		todo.date = date
		todo.reference_type = reference_type
		todo.reference_name = reference_name
		todo.insert(ignore_permissions=True)



@frappe.whitelist()
def create_interaction(doc):
		doc_json=json.loads(doc)
		# emp = frappe.db.get_value("Employee",{"user_id":doc_json['responsible']},"name")
		# doc_json['employee'] = emp
		"""allow any logged user to post a comment"""
		doc = frappe.get_doc(doc_json)

		if doc.doctype != "Interaction":
				frappe.throw(_("This method can only be used to create a Interaction Master"), frappe.PermissionError)

		doc.insert(ignore_permissions = True)

		return doc.as_dict()


@frappe.whitelist()
def add_expense(doc):
		doc_json=json.loads(doc)
		# emp = frappe.db.get_value("Employee",{"user_id":doc_json['responsible']},"name")
		# doc_json['employee'] = emp
		"""allow any logged user to post a comment"""
		doc = frappe.get_doc(doc_json)

		if doc.doctype != "Expense Claim":
				frappe.throw(_("This method can only be used to create a Expense Claim"), frappe.PermissionError)

		doc.insert(ignore_permissions = True)

		return doc.as_dict()