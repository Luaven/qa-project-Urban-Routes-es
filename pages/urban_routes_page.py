from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

"""
Paso 1. Localizar el ELEMENTO. Obtener la dirección del ELEMENTO.
        nombre_del_elemento = selector (By.SELECTOR, VALOR_DEL_SELECTOR)
        ejemplo: request_taxi_button = (By.CSS_SELECTOR, '.button.round')
               
Paso 2. Creo un Getter. Para definir un Getter debo crear un método para tomar el elemento.
        Agrego la palabra get_ y después el nombre de mi elemento.
        def get_request_taxi_button(self):
        Todos los Getter regresan el objeto.
        def get_request_taxi_button(self):
            return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )     
               
Paso 3. Debo definir la acción que voy a hacer con ese elemento. 
        setter -> Escribir -> En un input o en un text area
        clicker -> Dar click -> En un button y links
        reader -> Leer -> En cualquier elemento                  
"""

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    phone_number_button = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')  #Botón siguiente en la ventana emergente del número de teléfono
    id_code = (By.ID, 'code')
    confirm_button_phone = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    pay_method = (By.XPATH, '//div[@class="pp-text" and text()="Método de pago"]')
    add_card = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '#code.card-input')
    add_card_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    close_pay_method = (By.XPATH, "//div[@class='payment-picker open']//div[@class='modal']//button[@class='close-button section-close']")
    write_message = (By.ID, 'comment')
    blanket_button = (By.XPATH, '(//span[@class="slider round"])[1]')
    icecream_button = (By.XPATH, '(//div[@class="counter-plus" and text()="+"])[1]')
    take_taxi = (By.XPATH, '//button[@class="smart-button"]')
    #Estado inicial - Buscando conductor
    search_modal_title = (By.CLASS_NAME, "order-header-title")
    search_text = (By.XPATH, "//div[@class='order-header-title' and contains(text(), 'Buscar automóvil')]")
    #Estado final - Información del conductor
    driver_arrival_text = (By.XPATH, "//div[contains(text(), 'El conductor llegará en')]")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    #Paso 1. Configura la dirección
    def set_from(self, from_address):
        # self.driver.find_element(*self.from_field).send_keys(from_address)
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        # self.driver.find_element(*self.to_field).send_keys(to_address)
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    #Paso 2. Presiona botón Pedir un taxi
    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()
    #Paso 2. Selecciona la tarifa Comfort
    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )

    def click_on_comfort_icon(self):
        self.get_comfort_icon().click()

    #Paso 3. Presiona el botón de número de teléfono
    def get_phone_number_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click() #Aquí nos abre la ventana emergente para introducir el teléfono

    # Paso 3. Escribe en ventana emergente en el campo de número de teléfono
    def get_phone_field(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.phone_field)
        )

    def set_phone_number(self, phone_number):
        self.get_phone_field().send_keys(phone_number)

    def get_next_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_next_button(self):
        self.get_next_button().click()
    #Paso 3. Recibe el código al haber introducido el número de teléfono
    def get_id_code(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.id_code)
        )
    def set_id_code(self, code):
        self.get_id_code().send_keys(code)
    #Paso 3. Confirma el código en la ventana emergente del número de teléfono
    def get_confirm_button_phone(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.confirm_button_phone)
        )
    def click_confirm_button_phone(self):
        self.get_confirm_button_phone().click()

    #Paso 4. Agrega una tarjeta de crédito en botón Metodo de pago
    def get_pay_method(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.pay_method)
        )
    def click_on_pay_method(self):
        self.get_pay_method().click()
    #Paso 4. Seleccionar Agregar Tarjeta en ventana emergente Metodo de pago
    def get_add_card(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card)
        )
    def click_on_add_card(self):
        self.get_add_card().click()
    #Paso 4. Escribir el número de tarjeta y CVV
    def set_card_number_field(self, card_number):
        self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def set_card_code_field(self, card_code):
        cvv_field = self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        )
        cvv_field.send_keys(card_code)
        cvv_field.send_keys(Keys.TAB)

    def get_card_number_field(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')


    def get_card_code_field(self):
        return self.driver.find_element(*self.card_code_field).get_property('value')

    def set_card_data(self, card_number, card_code):
        self.set_card_number_field(card_number)
        self.set_card_code_field(card_code)

    def get_add_card_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_card_button)
        )
    #Paso 4. Agregar tarjeta como metodo de pago
    def click_add_card_button(self):
        self.get_add_card_button().click()

    #Paso 4. Cerrar ventana de agregar metodo de pago.
    def get_close_pay_method(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.close_pay_method)
        )
    def click_on_close_pay_method(self):
        self.get_close_pay_method().click()

    #Paso 5. Escribir un mensaje para el conductor
    def set_comment(self, comment_field):
        self.wait.until(
            EC.visibility_of_element_located(self.write_message)
        ).send_keys(comment_field)

    def get_comment_field(self):
        return self.driver.find_element(*self.write_message).get_property('value')

    def set_comment_data(self, message_for_driver):
        self.set_comment(message_for_driver)

    #Paso 6. Pedir una manta y pañuelos.
    def get_blanket_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.blanket_button)
        )
    def click_blanket_button(self):
        self.get_blanket_button().click()

    #Paso 7. Pedir 2 helados.
    def get_icecream_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.icecream_button)
        )
    def click_icecream_button(self):
        for i in range(2):
            self.get_icecream_button().click()

    #Paso 8. Aparece el modal para pedir un taxi
    def get_take_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.take_taxi)
        )
    def click_take_taxi_button(self):
        self.get_take_taxi_button().click()

    #Paso 9. Esperar a que aparezca la información del conductor en el modal
    def wait_for_driver_assignment(self):
        wait = WebDriverWait(self.driver, 60)  # Esperar hasta 60 segundos

        # Paso 1: Verificar que aparece el modal de búsqueda
        wait.until(EC.presence_of_element_located(self.search_text))
        print("✅ Modal de búsqueda apareció")

        # Paso 2: Esperar a que desaparezca el texto de búsqueda
        wait.until_not(EC.text_to_be_present_in_element(self.search_modal_title, "Buscar automóvil"))
        print("⏳ Búsqueda terminó")

        # Paso 3: Esperar a que aparezca la información del conductor
        driver_info = wait.until(EC.presence_of_element_located(self.driver_arrival_text))
        print("🚗 ¡Conductor asignado!")

        return driver_info

    def verify_driver_modal_transition(self):
        try:
            # Ejecutar la transición completa
            driver_info = self.wait_for_driver_assignment()

            # Verificar que el texto cambió correctamente
            arrival_text = driver_info.text
            assert "El conductor llegará en" in arrival_text

            return True
        except TimeoutException:
            print("❌ Timeout: No se encontró conductor en el tiempo esperado")
            return False








