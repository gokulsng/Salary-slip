import frappe
from datetime import datetime
from dateutil import parser


@frappe.whitelist()
def late_entry_check(self,method):
#	frappe.errprint(self)
#	shift = frappe.db.get_value("Shift Assignment",{"employee":self.employee},"shift_type")
#	shift_start_time = frappe.db.get_value("Shift Type",{"name":shift},"start_time")
	entry_time = parser.parse(self.time)
#	frappe.errprint(entry_time)
	time = datetime.strptime('1259','%H%M').time()
#	print(time)
	dt = datetime.strptime(self.time,"%Y-%m-%d %H:%M:%S").date()
	frappe.errprint(dt)
	dttime = datetime.combine(dt,time)
	frappe.errprint(dttime)
#	print(type(dttime))
	if entry_time > self.shift_start and entry_time < dttime:
		late =  entry_time - self.shift_start
		self.late_entry_time = round(float(late.seconds / 60),2)
#		frappe.errprint(self.late_entry_time)
 
