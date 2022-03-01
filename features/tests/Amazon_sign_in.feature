# Created by rima at 2/28/2022
Feature: Amazon Sign in tests
  After open Amazon.com use can see a sign_in popup and if user will click on that,
  User can see sign in page

  Scenario: Sign in page can be opened from sign in popup
    Given Open Amazon
    When click on sign in button from sign in popup
    Then verify sign in page opened.