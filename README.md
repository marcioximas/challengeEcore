# ChallengeECore - Test Automation Framework

This project is a **Test Automation Framework** designed using **Selenium**, **Behave** (a BDD tool), and **Python** for automating web-based applications. The framework follows the Page Object Model (POM) pattern, making it scalable and maintainable.

## Project Structure
challengeECore/ ├── features/ # Directory containing feature files (Gherkin scenarios) │ ├── pages/ # Page Object Model (POM) classes for web pages │ │ ├── init.py # Makes pages a package │ │ ├── base_page.py # Base class for all pages with common methods │ │ ├── home_page.py # Home page related actions and elements │ │ ├── invoice_details_page.py # Invoice details page actions and elements │ │ └── login_page.py # Login page actions and elements │ ├── steps/ # Step definitions for Behave scenarios │ └── tests/ # Directory for feature files and other test artifacts │ ├── .gitignore # Git ignore file for excluding unnecessary files ├── behave.ini # Behave configuration file ├── pytest.ini # pytest configuration file for integrations ├── requirements.txt # List of dependencies required for the project ├── run.py # Entry point for running the tests ├── report.html # Generated HTML report from the latest test run └── README.md # Project documentation (this file)

## Prerequisites

Ensure you have the following installed:

- **Python 3.6+**
- **pip** (Python package installer)
- **Google Chrome** and **chromedriver** (or equivalent browser and driver)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/marcioximas/challengeECore.git
   cd challengeECore

2. Install Dependencies: Use the following command to install the required Python packages from requirements.txt:

    pip install -r requirements.txt

3. Configure WebDriver:

Ensure that you have the correct WebDriver for your browser (e.g., chromedriver for Chrome).
Place the driver in your system path or specify the path directly in the test configuration.

Running Tests
Using Behave
To run the tests using Behave, run the following command:

bash
Copiar código
behave
If you want to run a specific feature file, specify the path:

bash
Copiar código
behave features/tests/sample.feature
Generating an HTML Report
After running the tests, you can view the HTML report in the report.html file. You can generate the report by running:

bash
Copiar código
pytest --html=report.html --self-contained-html
This will run the tests and create an HTML report in the root directory.

Using run.py as Entry Point
You can also execute the tests via the run.py script:

bash
Copiar código
python run.py
This script will trigger the test suite and generate an HTML report.

Project Structure Breakdown
Page Object Model (POM)
The Page Object Model pattern is implemented in the pages directory. Each page has its own Python class that encapsulates the elements and actions related to that page.

base_page.py: Contains common functionality for interacting with web elements such as waiting for elements, clicking, sending text, etc.
login_page.py: Contains locators and actions related to the login functionality.
home_page.py: Contains locators and actions for the home page.
invoice_details_page.py: Contains locators and actions for interacting with the invoice details page.
Features and Steps
features/steps: Contains step definitions written in Python to execute steps described in Gherkin files.
features/tests: Contains feature files written in Gherkin syntax, which describe the scenarios to be tested.

ontribution Guidelines
Fork the repository.
Create a new branch:
bash
Copiar código
git checkout -b feature-branch
Commit your changes:
bash
Copiar código
git commit -m "Add new feature"
Push the branch:
bash
Copiar código
git push origin feature-branch
Submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

bash
Copiar código

### Adjustments
- Replace `"marcioximas"` in the `git clone` command with your actual GitHub username or the appropriate repository URL.
- Adjust the **feature scenario** example in the "Example Test Scenario" section to match yo