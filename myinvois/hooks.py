app_name = "myinvois"
app_title = "myinvois"
app_publisher = "Rehan"
app_description = "myinvois"
app_email = "rehan.muhamad675@gmail.com"
app_license = "mit"

# required_apps = []

# Includes in <head>
# ------------------

fixtures = [
    
    {"dt": "Property Setter", "filters": [
                       
            ["module", "=", "myinvois"],
        ]},
    
    {"dt": "State"},
    {"dt": "Item Classification Codes"},
    {"dt": "Industrial Classification"},
    {"dt": "E-Invoice Types"},
    {"dt": "Taxable Types"},
    # {"dt": "DocType","filters": { "custom" : ["=", "1"], "name":"testing child table" }}
]




# include js, css files in header of desk.html
# app_include_css = "/assets/myinvois/css/myinvois.css"
# app_include_js = "/assets/myinvois/js/myinvois.js"

# include js, css files in header of web template
# web_include_css = "/assets/myinvois/css/myinvois.css"
# web_include_js = "/assets/myinvois/js/myinvois.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "myinvois/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
    "Sales Invoice" : "public/js/myinvois_sales_invoice.js",
    "Purchase Invoice" : "public/js/myinvois_purchase_invoice.js",
    "Lhdn Authorizations":  "public/js/myinvois_lhdn_authorizations.js"
    }

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "myinvois/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "myinvois.utils.jinja_methods",
# 	"filters": "myinvois.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "myinvois.install.before_install"
# after_install = "myinvois.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "myinvois.uninstall.before_uninstall"
# after_uninstall = "myinvois.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "myinvois.utils.before_app_install"
# after_app_install = "myinvois.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "myinvois.utils.before_app_uninstall"
# after_app_uninstall = "myinvois.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "myinvois.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# doc_events = {
# 	"Payment Entry": {
# 		"on_submit": "myinvois.utils.payment_entry.on_submit",
		
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"myinvois.tasks.all"
# 	],
# 	"daily": [
# 		"myinvois.tasks.daily"
# 	],
# 	"hourly": [
# 		"myinvois.tasks.hourly"
# 	],
# 	"weekly": [
# 		"myinvois.tasks.weekly"
# 	],
# 	"monthly": [
# 		"myinvois.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "myinvois.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "myinvois.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "myinvois.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["myinvois.utils.before_request"]
# after_request = ["myinvois.utils.after_request"]

# Job Events
# ----------
# before_job = ["myinvois.utils.before_job"]
# after_job = ["myinvois.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"myinvois.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# jenv = {
# 	"methods": [
# 		"gen_qrcode:myinvois.sign_invoice.gen_qrcode"
# 	]
# }

jinja = {
	"methods": [
		"myinvois.myinvois.sign_invoice.gen_qrcode"
	],
}