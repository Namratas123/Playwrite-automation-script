from pages.orangehrm_login_page import OrangeHRMLoginPage
from pages.orangehrm_pim_page import OrangeHRMPIMPage
import config.config as config
import uuid

def test_orangehrm_login_and_add_emp(page):
    login_page = OrangeHRMLoginPage(page)
    pim_page = OrangeHRMPIMPage(page)

    # Step 1: Login
    login_page.open(config.ORANGEHRM_URL)
    login_page.login(config.ORANGEHRM_USER, config.ORANGEHRM_PASSWORD)
    assert login_page.is_dashboard_visible()

    # Step 2: Go to Admin page
    pim_page.open_pim_page()

    # Step 3: Click Add User
    pim_page.click_user_details()

    # Step 4: Create employee
    unique_id = uuid.uuid4().hex[:5]
    pim_page.add_employee(
        first_name=f"Test{unique_id}",
        last_name="User"
    )