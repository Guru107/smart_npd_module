import frappe
from frappe.exceptions import FrappeTypeError

from smart_npd_module.tests import SmartNPDModuleTestSuite


class TestAPI(SmartNPDModuleTestSuite):
	def test_echo_returns_the_message(self) -> None:
		result = frappe.call("smart_npd_module.api.echo", message="hello")
		self.assertEqual(result, "hello")

	def test_echo_rejects_wrongly_typed_arguments(self) -> None:
		# A non-str `message` must not reach the method body. On v16 this
		# enforcement is gated by `require_type_annotated_api_methods` in
		# hooks.py; on v15 annotated whitelisted methods are always checked.
		with self.assertRaises(FrappeTypeError):
			frappe.call("smart_npd_module.api.echo", message=["not", "a", "string"])
