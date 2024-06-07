# Automation framework for Swag Labs
Python, Behave, Selenium WebDriver, Selenium Grid, Allure 

# Prerequisites
unix-like system  
python 3   
chromedriver (for Chrome)  
geckodriver (for FireFox)  
Selenium Grid

# Install requirements
`pip install -r requirements.txt`

# Run tests locally
Run locally (Chrome browser set by default)  
`behave saucedemo_bdd/tests/features/*.feature`  
Browser can be specified with 'browser' param  
`behave saucedemo_bdd/tests/features/products.feature -D browser=FIREFOX-LOCAL`  

# Run test with selenium grid
Lets say we would like to run tests in Chrome and Firefox in parallel
(you will need separate terminal window for each command)
1. start hub  
`java -jar selenium-server-<version>.jar hub`  
2. register two nodes (example for two browsers)  
`java -jar selenium-server-<version>.jar node --port 5555`  
`java -jar selenium-server-<version>.jar node --port 6666`  
3. run tests  
`behave saucedemo_bdd/tests/features/login.feature -D browser=FIREFOX-REMOTE`    
`behave saucedemo_bdd/tests/features/products.feature -D browser=CHROME-REMOTE`  

# Get allure report
Ideally need to be configured on CI/CD  
`allure serve`

# Configuration file    
`saucedemo_bdd/tests/config.yaml`.

