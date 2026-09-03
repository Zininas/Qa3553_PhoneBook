import pytest

from data.contact_data import create_contact
from pages.add_new_contact_page import ContactPage
from pages.contacts_page import ContactsPage


def test_delete_contact_success(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contacts_page.contact_card_visible(contact.phone)

    contacts_page.delete_contact(contact.phone)

    assert contacts_page.contact_cards_count(contact.phone) == 0


def test_delete_one_contact_leaves_others(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    first_contact = create_contact()
    second_contact = create_contact()

    contact_page.open_contact_form()
    contact_page.fill_contact_form(first_contact)
    contact_page.submit_contact()

    contact_page.open_contact_form()
    contact_page.fill_contact_form(second_contact)
    contact_page.submit_contact()

    assert contacts_page.contact_card_visible(first_contact.phone)
    assert contacts_page.contact_card_visible(second_contact.phone)

    contacts_page.delete_contact(first_contact.phone)

    assert contacts_page.contact_cards_count(first_contact.phone) == 0
    assert contacts_page.contact_card_visible(second_contact.phone)
