<!--
  * browser: architecture
  * version: 1.2.0
  * updated: 2020-02-17T02:39:34Z
  * contact: Shuai Wang (shuai.wang.kaos@gmail.com)
-->

# Project2 PyTest for API automation test

Use Selenium and framework PyTest to make the automation test, when tests complete the report will be generated in the project folder

Contents:

* [Why use PyTest test](#why-use-pytest-test)
* [The architecture information](#the-architecture-information)
* [Configure the enviroment](#configure-the-enviroment)
* [How to run the tests](#how-to-run-the-tests)


## Why use PyTest test

* It’s open-source and allows integration with a rich set of third-party plugins

* Allows execution of parallel tests

* Allows devs to run a specific test or a subset of tests

* PyTest supports all types of testing, it is primarily used for API and complex functional testing.


## The architecture information

The project has three folders to manage the project:

  * **..\Lib**
    *  the Lib folder manage the json files for the test uasage

  * **..\TestCases**
    * This folder contains all the automation tests

## Configure the enviroment:

  * Install pytest
    * use `pip install pytest`
    * the version is pytest 6.2.2

  * Install selenium
    * use `pip install selenium`
    * the version is selenium 3.141.0

  * Install jsonpath
    * use `pip install jsonpath`
    * the version is jsonpath 0.82

  * Install requests
    * use `pip install requests`
    * the version is requests 2.25.1

## How to run the tests:
  * you can the tests from command line with `pytest -v --html=report.html TestCases` from the path ..\ 
  * the report should be generated in the project folder
