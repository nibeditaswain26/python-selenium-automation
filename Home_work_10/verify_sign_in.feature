# Created by rima at 2/7/2022
Feature:Tests for Logged out user sees
        Sign in page when clicking Orders
  # Enter feature description here

  Scenario: User can see sign in page when clicking order
    Given Open Amazon
    When Click on Return&Order
    Then Verify sign in page opened