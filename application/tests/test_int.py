from selenium import webdriver
from flask import url_for
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from application import app, db
from application.models import Ideas, Tags
import os

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050

    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI=os.getenv('testdburi'), LIVESERVER_PORT=self.TEST_PORT, DEBUG=True, TESTING=True)
        return app

    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)
        db.create_all()
        t1 = Tags(name='Landscape')
        t2 = Tags(name='Portrait')
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()
        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()
        db.drop_all()

    def test_server_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class BasicTests(TestBase):
    def home_test(self):
        first_tag = self.driver.find_element_by_xpath('/html/body/h6[1]')
        self.assertEqual(first_tag, '1 Landscape')

    def add_test(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        input_box = self.driver.find_element_by_xpath('//*[@id="title"]')
        input_box.send_keys('Pilot')
        input_box = self.driver.find_element_by_xpath('//*[@id="description"]')
        input_box.send_keys('See if the pilot would take your camera for some shots inside the cockpit!')
        input_tag_id = driver.find_element_by_xpath('//*[@id="tag_id"]/option[2]').click()
        input_box = self.driver.find_element_by_xpath('//*[@id="name"]')
        input_box.send_keys('Peter')
        self.driver.find_element_by_xpath('//*[@id="submit"]')
        first_entry_title = self.driver.find_element_by_xpath('/html/body/p[1]')
        self.assertIn(first_entry_title, 'Pilot') 