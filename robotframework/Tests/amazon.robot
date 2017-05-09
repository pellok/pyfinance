*** Settings ***
Documentation  This is some info about the test cases(Test suit)
Library Selenium2Library

*** Test Cases ***
Navigating to amazon.in
    [Documentation]  opening amazon.in website
    [Tags]  sanity
    Open Browser  http://www.amazon.in gc
    Wait Until Page Contains  Your Amazon.in
    Close Browser