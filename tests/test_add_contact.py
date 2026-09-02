import random

from faker import Faker

from models.contact import Contact
from pages.add_contact_page import ContactPage

fake = Faker()

def test_add_contact_success_req_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name= fake.first_name(),
        last_name= fake.last_name(),
        phone= fake.numerify("050#########"),
        email= fake.unique.email(),
        address= fake.street_address(),
        description= fake.sentence(nb_words=5),
    )

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_req_fields_2(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        name= fake.first_name(),
        last_name= fake.last_name(),
        phone= fake.numerify("050#########"),
        email= fake.unique.email(),
        address= fake.city(),
        description= ""
    )

    contact_page.open_contact_form()
    contact_page.fill_contact(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)