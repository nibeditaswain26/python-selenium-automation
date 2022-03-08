# Created by rima at 2/28/2022
Feature: Amazon Sign in tests
  After open Amazon.com use can see a sign_in popup and if user will click on that,
  User can see sign in page

  Scenario: Sign in page can be opened from sign in popup
    Given Open Amazon
    When click on sign in button from sign in popup
    Then verify sign in page opened.

  Scenario: User can see signin in popup for few second.
    Given Open Amazon
    Then verify that sign in popup shown
    Then verify that sign in btn is clickable
    When wait for 4 sec
    Then verify that sign in popup shown
    Then  verify sign in popup disappears