import frappe

from smart_npd_module.tests import SmartNPDModuleTestSuite


class TestSmartNPDModuleSettings(SmartNPDModuleTestSuite):
	def test_settings_singleton_loads_with_default(self) -> None:
		settings = frappe.get_doc("Smart NPD Module Settings")
		self.assertEqual(settings.default_greeting, "Hello")

	def test_settings_singleton_save_and_reload(self) -> None:
		settings = frappe.get_doc("Smart NPD Module Settings")
		settings.default_greeting = "Hello from tests"
		settings.save()

		reloaded = frappe.get_doc("Smart NPD Module Settings")
		self.assertEqual(reloaded.default_greeting, "Hello from tests")
