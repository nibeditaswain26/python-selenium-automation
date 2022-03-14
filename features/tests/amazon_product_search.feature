# Created by rima at 3/14/2022
Feature: Tests for amazon search


  Scenario: User can search for a product
    Given Open Amazon
    When Search for "coffee"
    Then Verify search results are shown