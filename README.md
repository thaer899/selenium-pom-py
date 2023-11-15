[![test-selenium-multi-browser-manual](https://github.com/thaer899/selenium-pom-py/actions/workflows/test-selenium-multi-browser-manual.yml/badge.svg?branch=master)](https://github.com/thaer899/selenium-pom-py/actions/workflows/test-selenium-multi-browser-manual.yml)
[![test-selenium-single-browser-manual](https://github.com/thaer899/selenium-pom-py/actions/workflows/test-selenium-single-browser-manual.yml/badge.svg?branch=master)](https://github.com/thaer899/selenium-pom-py/actions/workflows/test-selenium-single-browser-manual)
[![test-selenium-multi-browser-multi-type](https://github.com/thaer899/selenium-pom-py/actions/workflows/test-selenium-multi-browser-multi-type.yml/badge.svg?branch=master)](https://github.com/thaer899/selenium-pom-py/actions/workflows/test-selenium-multi-browser-multi-type.yml)

### Selenium Testing using POM

This repository provides a comprehensive Selenium framework for web application testing using the Page Object Model (POM) design pattern.

#### Setup and Configuration

1. **Prerequisites**: Ensure a web browser and corresponding webdriver are installed. For Firefox on Windows, download the Gecko driver from [here](https://github.com/mozilla/geckodriver/releases). Install necessary Selenium packages with `pip install -r requirements.txt`.

2. **Driver Manager**: Initializes and manages Selenium web drivers in local and remote modes. Configurable for browsers like Firefox and Chrome using a central config file.

3. **Pages**: Base page is the Foundation for all page objects. Includes common web interactions like finding elements and navigating URLs. An example of a login page is there.

4. **Locators**: Centralizes all locators, grouped by page for easy management and updates.

5. **Selenium Tests**: Contains scripts to validate login functionality, including navigation, credential input, and post-login URL verification.

#### Workflows and Pipelines

1. **GitHub Workflows**: Set up under `tests/selenium/test_selenium_pom.py`:
   - **Single Browser Test Workflow**: For testing on a single browser (Firefox or Chrome).
   - **Multi-Browser Test Workflow**: Simultaneous testing on Firefox and Chrome.
   - **Multi-Browser and Multi-Type Test Workflow**: Testing on multiple browsers, both manually and via a cron job.

This setup provides a robust framework for Selenium testing, utilizing POM for efficient and effective test case management.
