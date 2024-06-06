# Automation framework for Swag Labs
Python, Behave, Selenium WebDriver, Selenium Grid, Allure 

# Prerequisites
Unix-like system with python 3 and pipenv installed  
Selenium Grid 'https://www.selenium.dev/documentation/grid/getting_started/'


# Install requirements
`pip install -r requirements.txt`

# Run all tests
`behave saucedemo_bdd/tests/features/*.feature`

# Get allure report
Ideally need to be configured on CI/CD  
`allure serve`

# Configure test browser
`BROWSER=FIREFOX-LOCAL make behave`  

# Configuration file    
`saucedemo_bdd/tests/config.yaml`.
