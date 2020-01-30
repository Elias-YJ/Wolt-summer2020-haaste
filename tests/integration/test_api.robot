*** Settings ***
Documentation    Suite description
Library        REST     http://127.0.0.1:5000/

*** Test Cases ***
Display all restaurants
    GET             /restaurants
    object          response body
    array           response body restaurants
    object          response body restaurants 0
    string          response body restaurants 0 name        "Social Burgerjoint Citycenter"
    [Teardown]      Output schema

