# Created by rima at 2/22/2022
Feature: Tests for Amazon best seller page
  # Enter feature description here

  Scenario: User can see 5 links in best seller page
    Given Open Amazon best seller page
    Then Verify user can see 5 links in best seller page

  Scenario: User can see correct page after click on the "Best Sellers" all links on the top menu.
    Given Open Amazon best seller page
    Then Verify that correct page opens when user go through all the best seller links