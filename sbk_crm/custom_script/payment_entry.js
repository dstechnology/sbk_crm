
frappe.ui.form.on("Payment Entry", "refresh", function(frm, doctype, name) {
cur_frm.add_custom_button(__('Add Meeting Details'), function(doc, cdt, cdn, cmnt) {
   var d = frappe.prompt([
    {'fieldname': 'person_interacted_with', 'fieldtype': 'Data', 'label': 'Person Interacted with', 'reqd': 0},    
    {'fieldname': 'type_of_interaction', 'fieldtype': 'Link', options:"Interaction Type",'label': 'Type of Interaction', 'reqd': 0},

    {'fieldname': 'responsible', 'fieldtype': 'Link', options:"User", 'default': user, 'label': 'Responsible', 'reqd': 0},
    {'fieldname': 'remarks', 'fieldtype': 'Text', 'label': 'Remarks', 'reqd': 1},

    {fieldtype: "Column Break"},
    {'fieldname': 'result', 'fieldtype': 'Link', options:"Interaction Result",'label': 'Result', 'reqd': 0},

    {'fieldname': 'next_date', 'fieldtype': 'Date', 
    'label': 'Next Action Date', 'default': frappe.datetime.add_days(frappe.datetime.nowdate(),7), 'reqd': 0},
    {'fieldname': 'next_action_by', 'fieldtype': 'Link', options:"User", 'default': user,'label': 'Next Action By', 'reqd': 0},
    {'fieldname': 'create_task', 'fieldtype': 'Check', 'default': true, 'label': 'Create Task'},

    {'fieldname': 'comment', 'fieldtype': 'Text', 'label': 'Next Action Task', 'reqd': 1},
    {fieldtype: "Section Break"},

    {fieldtype: "Section Break", collapsible:true},
    {'fieldname': 'is_expense', 'fieldtype': 'Check', 'label': 'Is Expense'},        
    {'fieldname': 'expense_type', 'fieldtype': 'Link', options:"Expense Claim Type",'label': 'Expense Claim Type', 'reqd': 0,depends_on:'is_expense'},
    {'fieldname': 'claim_amount', 'fieldtype': 'Currency', 'label': 'Expense Amount', 'reqd': 0,depends_on:'is_expense'},   
    {'fieldname': 'expense_date', 'fieldtype': 'Date', 
                'label': 'Expense Date', 'default': frappe.datetime.add_days(frappe.datetime.nowdate(),0), 'reqd': 1,depends_on:'is_expense'},
    {'fieldname': 'exp_approver', 'fieldtype': 'Link', options:"User", 'default': user,'label': 'Expense Approver', 'reqd': 0,depends_on:'is_expense'},
    {'fieldname': 'employee', 'fieldtype': 'Link', options:"Employee" ,'label': 'From Employee',depends_on:'is_expense'},  
   
    {fieldtype: "Column Break"},
    {'fieldname': 'description', 'fieldtype': 'Text', 'label': 'Description',depends_on:'is_expense'},  
    
    ],
    function(values){
    var c = d.get_values()
    var cmnt =  "Person Interacted with: "+ c.person_interacted_with
               +"<br>Type of Interaction: "+ c.type_of_interaction
               +"<br>Result: "+ c.result
               +"<br>Next Action Date: " +frappe.format(frappe.datetime.now_date(),{'fieldtype':'Date'})

               +"<br>Next Action By: "+ c.next_action_by 
               +"<br>Next Action Task: "+c.comment
               +"<br>Responsible: "+c.responsible
               +"<br>Remarks: "+c.remarks
               if (c.is_expense == true) {
               var c = d.get_values()
               var cmnt = 
                           "Person Interacted with: "+ c.person_interacted_with
                           +"<br>Type of Interaction: "+ c.type_of_interaction
                           +"<br>Result: "+ c.result
                           +"<br>Next Action Date: " +frappe.format(frappe.datetime.now_date(),{'fieldtype':'Date'})
                           +"<br>Next Action By: "+ c.next_action_by 
                           +"<br>Next Action Task: "+c.comment
                           +"<br>Responsible: "+c.responsible
                           +"<br>Remarks: "+c.remarks
                           +"<br>Expense Claim Type: "+c.expense_type
                           +"<br>Expense Amount: "+c.claim_amount
                           +"<br>Expense Date: "+frappe.format(frappe.datetime.now_date(),{'fieldtype':'Date'})
                           +"<br>Description: "+c.description 
                           +"<br>From Employee: "+c.employee
                           +"<br>Expense Approver: "+c.exp_approver
               }
            
    var me = frm.doc
    if(c.is_expense == true) {
        frappe.call({
            method: "sbk_crm.custom_methods.add_expense",
            args: {
                doc:{
                    doctype: "Expense Claim",
                    // reference_doctype: frm.doc.doctype,
                    // reference_name: me.name,
                    // type_of_interaction: c.type_of_interaction,
                    // result: c.result,
                    // responsible: c.responsible,
                    // person_interacted_with: c.person_interacted_with,
                    // next_date: c.next_date,
                    // next_action_by: c.next_action_by,
                    // comment: c.comment,
                   
                    "expenses":[{
                                    
                                    "expense_type": c.expense_type,
                                    "expense_date": c.expense_date,
                                    "claim_amount": c.claim_amount,
                                    "description": c.description,
                                    "sanctioned_amount": c.sanctioned_amount,
                                }
                                ],
                    employee: c.employee,
                    exp_approver: c.exp_approver,
                   
                }
            },

            callback: function(r) {
                    frappe.msgprint("Expense Quotation record created");
        

        }

        });
    }
     // start interaction master
        frappe.call({
            method: "sbk_crm.custom_methods.create_interaction",
            args: {
                doc:{
                    doctype: "Interaction",
                    reference_doctype: frm.doc.doctype,
                    reference_name: frm.doc.name,
                    result: c.result,
                    person_interacted_with: c.person_interacted_with,

     //                responce_reson: c.responce_reson,
                    next_action_date: c.next_date,
                    type_of_interaction: c.type_of_interaction,
                    result: c.result,
                    next_action_by: c.next_action_by,
                    next_action_task: c.comment,
                    remarks: c.remarks,
                    responsible: c.responsible
                    // next_date
                }
            },
            callback: function(r) {
                        msgprint("Interaction master record created");
            }
        });
        //new code
        console.log(c.create_task);
        if(c.create_task==true){
            frappe.call({
                            method: "sbk_crm.custom_methods.create_todo",
                            args: {
                                owner: c.next_action_by,
                                assigned_by: c.responsible,
                                description: c.comment,
                                date: c.next_date,
                                reference_name: frm.doc.name,
                                reference_type: frm.doc.doctype
                            }
                        });
        }
                // end of create todo
        return frappe.call({
                method: "frappe.desk.form.utils.add_comment",
                args: {
                    doc:{
                        doctype: "Communication",
                        communication_type: "Comment",
                        reference_doctype: frm.doc.doctype,
                        reference_name: frm.doc.name,
                        comment: "cmnt",
                        subject: "cmnt",
                        content: cmnt,
                        responce_reson: c.responce_reson,
                        next_date: c.next_date,
                        type_of_interaction: c.type_of_interaction,
                        result: c.result,
                        next_action_by: c.next_action_by,
                        comment_by: user
                    }
                },
                callback: function(r) {
                            msgprint("Interaction Submited Successfully");
                            cur_frm.reload_doc();

                if (cur_frm) {
                            if (cur_frm.docname && (frappe.last_edited_communication[cur_frm.doctype] || {})[cur_frm.docname]) {
                                delete frappe.last_edited_communication[cur_frm.doctype][cur_frm.docname];
                            }
                            // cur_frm.comments.input.val("");
                        }
                }
            });
                //new code
                

    },
    //functon
    'Type of Interaction',
    'Submit','Expense Claim', "btn-default"
    )
});

});