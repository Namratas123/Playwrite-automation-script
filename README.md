# OrangeHRM UI Test Automation (Playwright + Python + PyTest)

End-to-end UI test automation for the [OrangeHRM open-source demo](https://opensource-demo.orangehrmlive.com/) application, built with **Playwright (Python)** and **PyTest** using the **Page Object Model (POM)** design pattern.

The project demonstrates a clean, maintainable automation structure: reusable page classes, centralised configuration, a shared browser fixture, and unique test data generated on every run.

## What is tested

| Test | Flow |
|------|------|
| `test_orangehrm_login_and_add_emp` | Log in as Admin, verify the Dashboard loads, open the **PIM** module, click **Add**, create a new employee with a unique name, and verify the **Personal Details** page opens after saving |

## Tech stack

- **Language:** Python 3.11
- **Automation:** Playwright (sync API), Chromium
- **Test runner:** PyTest
- **Design pattern:** Page Object Model
- **Reporting config:** Playwright HTML reporter, screenshots/video on failure (see `playwright.config.ts`)

## Project structure

```
.
├── config/
│   └── config.py                  # App URL and demo credentials
├── pages/
│   ├── orangehrm_login_page.py    # Login page object (locators + actions)
│   └── orangehrm_pim_page.py      # PIM / Add Employee page object
├── tests/
│   └── test_orangehrm_login.py    # Login + add employee test
├── conftest.py                    # PyTest fixture that launches/closes the browser
├── pytest.ini                     # PyTest defaults (verbose, headed, testpaths)
└── playwright.config.ts           # Playwright reporter/artifact settings
```

## Key design points

- **Page Object Model:** locators and page actions live in `pages/`, so tests read like the user journey and UI changes are fixed in one place.
- **Reusable browser fixture:** `conftest.py` provides a function-scoped `page` fixture, so every test gets a fresh browser context and clean teardown.
- **Centralised configuration:** URL and credentials are kept in `config/config.py`, not hard-coded in tests.
- **Unique test data:** employee names are generated with `uuid`, so the test can run repeatedly without clashing with existing records.
- **Built-in waits and assertions:** uses Playwright's `expect(...)` auto-waiting assertions and explicit waits instead of fixed sleeps.

## Getting started

**Prerequisites:** Python 3.11+

```bash
# 1. Clone the repository
git clone https://github.com/Namratas123/Playwrite-automation-script.git
cd Playwrite-automation-script

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install pytest playwright
playwright install chromium
```

## Running the tests

```bash
# Run all tests (headed mode, verbose - set in pytest.ini)
pytest

# Run a single test file
pytest tests/test_orangehrm_login.py
```

## Notes

- The tests run against the public OrangeHRM demo site, which uses shared demo credentials (`Admin` / `admin123`) published by OrangeHRM. No private data is used.
- The demo site is shared and can occasionally be slow or reset; re-run if a test times out.

## Author

**Namrata** - QA Automation Engineer
Skills: Playwright, Selenium, PyTest, Robot Framework, Postman, JMeter, Python, JavaScript, Git/GitHub

Feel free to connect or open an issue with feedback.
