# Created by Lenno at 10/12/2020
Feature: Pruebas Flink

  @Prueba_Saucedemo
  Scenario: Funcionalidades de Saucedemo
    Given Open the aplication
    When I chargen the Jsom of the App: saucedemo.json
    Then I enter the user's data
    And I click on the login button
    Then I add the Sauce Labs Backpack and Sauce Labs Fleece products to the cart Jacket
    Then I go to cart
    And  Validating the name of the products
    Then I remove the last product from the cart
    Then I click the CHECKOUT button
    And I fill in the user information and click on the CONTINUE button
    Then Valid the Error: Postal Code is required
    Then I enter the zip code and click on the CONTINUE button
    And I click the FINISH button
    Then I validate the message THANK YOU FOR YOUR ORDER