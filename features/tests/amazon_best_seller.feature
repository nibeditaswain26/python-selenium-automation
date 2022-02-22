# Created by rima at 2/22/2022
Feature: Tests for Amazon best seller page
  # Enter feature description here

  Scenario: User can see 5 links in best seller page
    Given Open Amazon best seller page
    Then Verify user can see 5 links in best seller page