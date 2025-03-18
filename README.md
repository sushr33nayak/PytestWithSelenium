# Pytest Selenium Project

## Overview
This project is a test automation framework using **Pytest** and **Selenium** to automate web applications. It supports running UI tests efficiently with parallel execution, reporting, and cross-browser testing.

## Features
- **Pytest-based framework** for easy test execution and reporting
- **Selenium WebDriver** for web UI automation
- **Parallel test execution** using pytest-xdist
- **Cross-browser testing** (Chrome, Firefox, Edge, etc.)
- **Logging and reporting** with pytest-html and allure reports
- **Page Object Model (POM) implementation** for maintainable tests

## Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Google Chrome / Firefox / Edge (based on testing requirements)
- ChromeDriver / GeckoDriver / EdgeDriver
- Virtual Environment (optional but recommended)

## Installation
Clone the repository:
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Create and activate a virtual environment (optional but recommended):
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Project Structure
```
project-root/
|-- tests/                    # Test cases directory
|   |-- test_example.py        # Sample test case
|-- pages/                    # Page Object Model classes
|   |-- base_page.py           # Base page containing common functions
|   |-- login_page.py          # Example page class
|-- utils/                    # Utility functions
|-- conftest.py               # Configuration and fixtures
|-- pytest.ini                # Pytest configuration file
|-- requirements.txt          # Dependencies
|-- README.md                 # Project documentation
```

## Running Tests
Run all tests:
```sh
pytest
```

Run tests with detailed output:
```sh
pytest -v
```

Run tests in parallel:
```sh
pytest -n 4  # Run tests in 4 parallel threads
```

Run tests with HTML report:
```sh
pytest --html=report.html --self-contained-html
```

Run tests with Allure report:
```sh
pytest --alluredir=allure-results
allure serve allure-results
```

## Writing Tests
Create a test case inside the `tests/` directory:
```python
from pages.login_page import LoginPage

def test_login_valid_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("testuser", "password")
    assert login_page.is_logged_in()
```

## Configurations
Customize the `pytest.ini` file to configure pytest settings:
```ini
[pytest]
addopts = -v --tb=short
log_cli = true
log_level = INFO
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a pull request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

