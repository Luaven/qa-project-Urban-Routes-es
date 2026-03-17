from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data import data
from data.data import phone_number
from helpers.utilities import retrieve_phone_code
from pages.urban_routes_page import UrbanRoutesPage


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_select_comfort_tariff(self):
        self.routes_page.click_on_request_taxi_button()
        self.routes_page.click_on_comfort_icon()

    def test_set_phone_number(self):
        self.routes_page.click_on_phone_number_button()
        self.routes_page.set_phone_number(phone_number)

    def test_get_next_button(self):
        self.routes_page.click_next_button()
        code = retrieve_phone_code(self.driver)
        self.routes_page.set_id_code(code)

    def test_confirm_button_phone(self):
        self.routes_page.click_confirm_button_phone()

    def test_pay_method_button(self):
        self.routes_page.click_on_pay_method()

    def test_add_card(self):
        self.routes_page.click_on_add_card()

    def test_set_card(self):
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_card_data(card_number, card_code)
        assert self.routes_page.get_card_number_field() == card_number
        assert self.routes_page.get_card_code_field() == card_code

    def test_add_button_full(self):
        self.routes_page.click_add_card_button()

    def test_close_pay_method(self):
        self.routes_page.click_on_close_pay_method()

    def test_comment_field(self):
        message_for_driver = data.message_for_driver
        self.routes_page.set_comment_data(message_for_driver)
        assert self.routes_page.get_comment_field() == message_for_driver

    def test_blanket_button(self):
        self.routes_page.click_blanket_button()

    def test_icecream_button(self):
        self.routes_page.click_icecream_button()

    def test_take_taxi_button(self):
        self.routes_page.click_take_taxi_button()
        driver_modal_success = self.routes_page.verify_driver_modal_transition()
        assert driver_modal_success, "No se pudo verificar la información del conductor"


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()