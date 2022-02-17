# Created by rima at 2/14/2022
Feature:Test to search for solutions of Canceling an order on Amazon
  # Enter feature description here

  Scenario: User can see cancel item and order page when search for canceling order
    Given Open Amazon help page
    When Use search help library field and search for Cancel order and Hitting keyboard ENTER btn with send_keys command
    Then Verify that 'Cancel items or orders' text is present
