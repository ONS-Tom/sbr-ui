# This file contains any commonly used constants used within the Selenium tests
# e.g. button/input IDs, URLs etc.

# Authentication
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'
INVALID_USERNAME = 'abc'
INVALID_PASSWORD = 'abc'

# Input IDs
USERNAME_INPUT_ID = 'usernameInput'
PASSWORD_INPUT_ID = 'passwordInput'
SEARCH_INPUT_ID = 'referenceNumberInput'
UNIT_TYPE_INPUT_ID = 'unitTypeInput'
PERIOD_INPUT_ID = 'periodInput'
LOGIN_BUTTON_ID = 'loginButton'
LOGOUT_BUTTON_ID = 'logoutButton'
SEARCH_BUTTON_ID = 'searchButton'

# Text IDs
SEARCH_TITLE_ID = 'homeTitle'
LOGIN_TITLE_ID = 'loginTitle'
SBR_DESCRIPTION_ID = 'sbrDescriptionText'

# Breadcrumb IDs
BREADCRUMB_SEARCH_ID = 'breadcrumbSearchLink'
BREADCRUMB_SELECTED_ID = 'breadcrumbCurrentUnit'
BREADCRUMB_ENT_ID = 'breadcrumbEnt'
BREADCRUMB_LEU_ID = 'breadcrumbLeu'

# Child Links IDs
CHILD_LINKS_TABS_ID = 'childLinksTabs'
LEU_TAB = 'leuTab'
REU_TAB = 'reuTab'
LOU_TAB = 'louTab'
CH_TAB = 'chTab'
VAT_TAB = 'vatTab'
PAYE_TAB = 'payeTab'
LEU_CHILD_TABLE = 'leuChildLinksTable'
REU_CHILD_TABLE = 'reuChildLinksTable'
LOU_CHILD_TABLE = 'louChildLinksTable'
CH_CHILD_TABLE = 'chChildLinksTable'
VAT_CHILD_TABLE = 'vatChildLinksTable'
PAYE_CHILD_TABLE = 'payeChildLinksTable'

# Unit Page Content
UNIT_NAME_ID = 'unitName'
UNIT_BADGE_ID = 'unitBadge'
UNIT_ID_ID = 'unitId'

# URLs
PROTOCOL = 'http'
PORT = '5000'
HOST_NAME = 'localhost'
BASE_URL = f'{PROTOCOL}://{HOST_NAME}:{PORT}'
LOGIN_URL = f'{BASE_URL}/Login'
SEARCH_URL = f'{BASE_URL}/Search'
ERROR_URL = f'{BASE_URL}/Error'

# Unit Types
ENTERPRISE = 'ENT'
LEGAL_UNIT = 'LEU'
REPORTING_UNIT = 'REU'
LOCAL_UNIT = 'LOU'
COMPANY_HOUSE = 'CH'
VALUE_ADDED_TAX = 'VAT'
PAY_AS_YOU_EARN = 'PAYE'

# Search
PERIOD = '201810'
ERN = '1234567890'
UBRN = '7584930284759231'
LURN = '849204991'
CRN = '44599148'
PAYEREF = '736FB28947'
VATREF = '663828891038'
RURN = '78391432987'



