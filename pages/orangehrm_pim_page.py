from playwright.sync_api import expect

class OrangeHRMPIMPage:
    def __init__(self, page):
        self.page = page

        # Left side Admin menu
        self.pim_menu = page.locator("span:has-text('PIM')")
        # Page heading
        self.pim_header = page.locator("h6:has-text('PIM')")

       # Add button
        self.add_button = page.locator("button:has-text('Add')")

        # Form fields
        self.first_name = page.locator('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')
        self.last_name = page.locator('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')
 

        # Save button
        self.save_button = page.locator("button:has-text('Save')")

        self.personal_details_header = page.locator(
            "h6:has-text('Personal Details')"
        )

    def open_pim_page(self):
        self.pim_menu.click()
        expect(self.pim_header).to_be_visible()

    def click_user_details(self):
        self.add_button.click()
        expect(self.page.locator("h6:has-text('Add Employee')")).to_be_visible()

    def add_employee(self, first_name, last_name):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.save_button.click()
   
    
        expect(self.personal_details_header).to_be_visible()
        self.page.wait_for_load_state("networkidle")



