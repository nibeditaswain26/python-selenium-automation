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

  Scenario: User can see language options
    Given Open Amazon
    When Hover over the language options
    Then Verify spanish option is present

  Scenario Outline: User can select and search in a department
    Given Open Amazon
    When select department by alias <alias>
    And Search for <search_word>
    Then Verify <department> department is selected
    Examples:
    |alias         |search_word       |department  |
    |stripbooks    |faust             |books       |
    |audible       |harry potter      |audible     |
    |pets          |treats            |pet-supplies |