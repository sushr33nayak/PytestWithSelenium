# Selenium Pytest Automation Framework

This repository contains Selenium WebDriver automated tests written in Python using Pytest. The tests run in **headless Chrome** mode and are integrated with GitHub Actions for continuous testing triggered manually via workflow dispatch.

---

## Features

- Selenium WebDriver configured for **headless Chrome**  
- Test automation framework built on **Pytest**  
- Generates detailed **HTML reports**  
- Integrated with **GitHub Actions** for CI/CD with manual trigger  
- Reports uploaded as artifacts for easy download and review  
- Test result summaries displayed in GitHub Checks UI  

---

## Project Structure

    project-root/
    |-- tests/                    # Test cases directory
    |   |-- test_example.py       # Sample test case
    |-- conftest.py               # Pytest configuration and fixtures
    |-- pytest.ini                # Pytest settings
    |-- requirements.txt          # Python dependencies
    |-- README.md                 # Project documentation
    |-- .github/
        |-- workflows/
            |-- run-pytests.yml   # GitHub Actions workflow file

---

## Setup & Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   
## Install required dependencies:
pip install -r requirements.txt

## Running Tests Locally
pytest tests/ --html=report.html --self-contained-html 

## GitHub Actions Integration
1.Tests run in headless Chrome on GitHub’s Ubuntu runners.

2.Workflow is manually triggered via workflow_dispatch in the Actions tab.

3.Generates and uploads  HTML reports as workflow artifacts.

4.GitHub parses HTML to display test results summary in Checks UI.

## How to trigger the workflow
1.Navigate to the Actions tab in the repo.

2.Select the Run Pytests workflow.

3.Click Run workflow and choose the branch.

4.Monitor the workflow and download reports from artifacts.

## Viewing Test Reports
1.GitHub UI shows test summary via the HTML report.

2.Download the HTML report artifact for a full, formatted test report.

