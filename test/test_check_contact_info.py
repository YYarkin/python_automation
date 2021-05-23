import re
from random import randrange


def test_check_contact_info_on_home_page(app):
    home_page_contacts = app.contact.get_contact_list()
    index = randrange(len(home_page_contacts))
    contact_from_home_page = home_page_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub('[() -]', "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [
        contact.home_phone, contact.mobile_phone, contact.work_phone, contact.second_phone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [
        contact.email1, contact.email2, contact.email3])))
