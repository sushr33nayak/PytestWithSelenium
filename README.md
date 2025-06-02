# Selenium Pytest Automation Framework

This repository contains Selenium WebDriver automated tests written in Python using Pytest. The tests run in **headless Chrome** mode and are integrated with GitHub Actions for continuous testing triggered manually via workflow dispatch.

---

## Features

- Selenium WebDriver configured for **headless Chrome**
- Test automation framework built on **Pytest**
- Supports **Page Object Model (POM)** design pattern
- Generates detailed **JUnit XML** and **HTML reports**
- Integrated with **GitHub Actions** for CI/CD with manual trigger
- Reports uploaded as artifacts for easy download and review
- Test result summaries displayed in GitHub Checks UI

---

## Project Structure

project-root/
|-- tests/ # Test cases directory
| |-- test_example.py # Sample test case
|-- pages/ # Page Object Model classes
| |-- base_page.py # Base page containing common functions
| |-- login_page.py # Example page class
|-- conftest.py # Pytest configuration and fixtures
|-- pytest.ini # Pytest settings
|-- requirements.txt # Python dependencies
|-- README.md # Project documentation
|-- .github/
|-- workflows/
|-- run-pytests.yml # GitHub Actions workflow file

yaml
Copy
Edit

---

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Running Tests Locally
Execute all tests with HTML and JUnit XML reports generated:

bash
Copy
Edit
pytest tests/ --html=report.html --self-contained-html --junitxml=report.xml -v
Open report.html in a browser to view a detailed, human-readable report.

GitHub Actions Integration
Tests are automatically run in GitHub Actions when manually triggered via the Actions tab.

Tests run in a headless Chrome environment.

Generates and uploads JUnit XML and HTML test reports as artifacts.

Test summaries are displayed in the GitHub Checks tab.

How to trigger the workflow
Go to the Actions tab in this repository.

Select the Run Pytests workflow.

Click Run workflow and select the branch.

Monitor the test run and check artifacts for reports.

HTML report can be downloaded from the workflow artifacts for a comprehensive visual report.

Contributing
Contributions and suggestions are welcome! Feel free to open issues or submit pull requests.