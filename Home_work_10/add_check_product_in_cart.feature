# Created by rima at 2/22/2022
Feature: Tests to add any product into the cart, and make sure it’s there
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given Open Amazon
    When Search for Urban Decay Naked Eyeshadow Palette
    And Clik on the First product
    And Store the product name
    And click on add to cart button
    And Open cart page
    Then verify cart has 1 item(s)
    And verify cart has correct product
