class OrangeHRMLoginPage:
    def __init__(self, page):
        self.page = page
#login to orangeHRM and redirect to Dasboard 
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        self.dashboard_header = page.locator("h6:has-text('Dashboard')")

    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()


    def is_dashboard_visible(self):
        self.dashboard_header.wait_for(timeout=10000)
        return self.dashboard_header.is_visible()