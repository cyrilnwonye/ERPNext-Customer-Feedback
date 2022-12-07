import frappe 

@frappe.whitelist(allow_guest=True)
def get_customer_feedback(**kwargs):
    
    delivery_note_number = kwargs['delivery_note_number']
    
    customer_name, contact_person = frappe.get_value("Delivery Note", delivery_note_number, ["customer", "contact_person"])
    email_address = frappe.get_value("Contact Email", {"parent": contact_person}, ["email_id"])
            
    
    feedback = frappe.get_doc({
        "doctype": "Delivery Customer Feedback",
        "delivery_note_number": kwargs['delivery_note_number'],
        "customer": customer_name,
        "customer_contact_name": customer_name,
        "customer_contact_email": email_address,        
        "was_the_goods_orand_services_delivered": kwargs['service_well_delivered'],
        "general_service_delivery": kwargs['general_service'],
        "timelines_of_service_delivery": kwargs['timeliness'],
        "personnel_technical_effectiveness": kwargs['personal_effectiveness'],
        "personnel_communication_skill": kwargs['personal_communication'],
        "what_did_we_do_well": kwargs['did_well'],
        "what_could_we_improve": kwargs['can_improve'],
        "please_state_any_additional_supportservice_required": kwargs['additional']
    })
    
    try:
        feedback.insert(ignore_permissions=True)
        frappe.db.commit()
        
        response = "Your feedback has been received! Thank you."

    except Exception as e:
        response = str(e)
    
    return response