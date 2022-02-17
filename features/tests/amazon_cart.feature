# Created by rima at 2/14/2022
Feature: Tests to check amazon cart is empty
  # Enter feature description here

  Scenario: User can see empty cart when click on cart icon
    Given Opens Amazon
    When clicks on the cart icon
    Then verifies that Your Amazon Cart is empty