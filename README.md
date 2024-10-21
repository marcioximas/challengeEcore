# ChallengeECore - Test Automation Framework

This project is a **Test Automation Framework** designed using **Selenium**, **Behave** (a BDD tool), and **Python** for automating web-based applications. The framework follows the Page Object Model (POM) pattern, making it scalable and maintainable.

## Project Structure
challengeECore/   
   ├── features/ # Directory containing feature files (Gherkin scenarios)  
   ├── pages/ # Page Object Model (POM) classes for web pages  
   ├── steps/ # Step definitions for Behave scenarios      
   ├── .gitignore # Git ignore file for excluding unnecessary files   
   ├── behave.ini # Behave configuration file  
   ├── pytest.ini # pytest configuration file for integrations  
   ├── requirements.txt # List of dependencies required for the project  
   ├── run.py # Entry point for running the tests  
   ├── report.html # Generated HTML report from the latest test run  
   └── README.md # Project documentation (this file)

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
   ```bash
    pip install -r requirements.txt

3. Configure WebDriver:

Ensure that you have the correct WebDriver for your browser (e.g., chromedriver for Chrome).
Place the driver in your system path or specify the path directly in the test configuration.

## Running the Tests
To run the tests using Behave, run the following command:

   ```bash
     behave
     
```` 
If you want to run tests using one or more tags, run the following command:

   ```bash
     behave -t "@tagname"
     
```` 
If you want to run it with an HTML report, you can use the following command:

```bash
behave -f behave_html_formatter:HTMLFormatter -o report.html
````
At the end, you will find the report.html file in the root of the project. See the example below:
[Report](report.html)


### Contact Information 

- Email: marcioximas@gmail.com
- Linkedin: https://www.linkedin.com/in/marcio-ximenes/
