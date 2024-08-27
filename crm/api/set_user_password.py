# /home/frappe/frappe-bench/apps/crm/crm/api/set_user_password.py

import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def set_user_password(user_name, encrypted_password):
    try:
        # Actualizar la contraseña en la base de datos
        frappe.db.sql("""insert into `__Auth` (doctype, name, fieldname, `password`)
                         values ('User', %(name)s, 'password', %(password)s)
                         on duplicate key update `password`=%(password)s""",
                         {'name': user_name, 'password': encrypted_password})
        frappe.db.commit()
        return {"status": "success", "message": "Contraseña actualizada correctamente"}
    except Exception as e:
        frappe.log_error(message=str(e), title="Error al actualizar la contraseña")
        return {"status": "error", "message": "No se pudo actualizar la contraseña"}
