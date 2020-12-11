# -*- coding: utf-8 -*-
import time

from behave import *
from selenium.webdriver import ActionChains

from src.fuctions.Functions import Functions as Saucedemo
from selenium.webdriver.common.by import By

use_step_matcher("re")

class Saucedemo_prueba(Saucedemo):
    @given("Open the aplication")
    def abrir_navegador(self):
        Saucedemo.abrir_navegador(self)

        time.sleep(5)


    @when("I chargen the Jsom of the App: saucedemo\.json")
    def cargo_json(self):
        Saucedemo.get_json_file(self, "saucedemo")


    @then("I enter the user's data")
    def datos_usuario(self):
        usuario = "standard_user"
        password = "secret_sauce"

        Saucedemo.get_elements(self, "nombre_usuario").send_keys(usuario)
        Saucedemo.get_elements(self, "usuario_pass").send_keys(password)

        time.sleep(3)


    @step("I click on the login button")
    def step_impl(self):
        Saucedemo.get_elements(self, "btn_login").click()
        time.sleep(5)


    @then("I add the Sauce Labs Backpack and Sauce Labs Fleece products to the cart Jacket")
    def step_impl(self):

        localizador = self.driver.find_element(By.XPATH,
                                               "/html/body/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/button")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        time.sleep(2)

        Saucedemo.get_elements(self, "btn_ADD_CART1").click()
        time.sleep(3)

        localizador = self.driver.find_element(By.XPATH,
                                               "/html/body/div/div[2]/div[2]/div/div[2]/div/div[4]/div[3]/button")
        action = ActionChains(self.driver)
        action.move_to_element(localizador)
        time.sleep(2)

        Saucedemo.get_elements(self, "btn_ADD_CART2").click()
        time.sleep(3)


    @then("I go to cart")
    def step_impl(self):
        Saucedemo.get_elements(self, "Carrito").click()
        time.sleep(5)


    @step("Validating the name of the products")
    def step_impl(self):

        assert Saucedemo.get_text(self, "Nom_Producto01") == "Sauce Labs Backpack"
        assert Saucedemo.get_text(self, "Nom_Producto02") == "Sauce Labs Fleece Jacket"
        time.sleep(2)


    @then("I remove the last product from the cart")
    def step_impl(self):
        Saucedemo.get_elements(self, "Remuevo_Ultimo_Prod").click()
        time.sleep(2)


    @then("I click the CHECKOUT button")
    def step_impl(self):
        Saucedemo.get_elements(self, "btn_CHECKOUT").click()
        time.sleep(3)



    @step("I fill in the user information and click on the CONTINUE button")
    def step_impl(self):
        first_name = "Eleno"
        last_name = "Ramirez Guzman"

        Saucedemo.get_elements(self, "Info_Nombre_Usuario").send_keys(first_name)
        Saucedemo.get_elements(self, "Info_Apellido_Usuario").send_keys(last_name)
        time.sleep(3)

        Saucedemo.get_elements(self, "btn_CONTINUE").click()
        time.sleep(1)


    @then("Valid the Error: Postal Code is required")
    def step_impl(self):
        assert Saucedemo.get_text(self, "Error_Codigo_Postal") == "Error: Postal Code is required"
        time.sleep(2)



    @then("I enter the zip code and click on the CONTINUE button")
    def step_impl(self):
        postal_code = "1234"

        Saucedemo.get_elements(self, "Info_Codigo_Postal").send_keys(postal_code)
        time.sleep(2)

        Saucedemo.get_elements(self, "btn_CONTINUE").click()


    @step("I click the FINISH button")
    def step_impl(self):
        Saucedemo.get_elements(self, "btn_FINISH").click()
        time.sleep(3)


    @then("I validate the message THANK YOU FOR YOUR ORDER")
    def step_impl(self):
        assert Saucedemo.get_text(self, "Mensaje_Final") == "THANK YOU FOR YOUR ORDER"
        time.sleep(5)