import re
from functools import reduce
from random import randrange


def test_compare_contact_info_on_home_page_with_db(app, db):
    home_page_contacts = app.contact.get_contact_list()
    db_contacts = db.get_contact_list()
    assert len(home_page_contacts) == len(db_contacts)
    for contact_from_home_page in home_page_contacts:
        # for contact_from_db in db_contacts:
        #   if contact_from_db.id == contact_from_home_page.id:
        #       break
        contact_from_db = reduce(lambda x: x[0], filter(lambda x: x.id == contact_from_home_page.id, db_contacts))
        assert contact_from_home_page.firstname == merge_like_on_home_page(contact_from_db.firstname)
        assert contact_from_home_page.lastname == merge_like_on_home_page(contact_from_db.lastname)
        assert contact_from_home_page.address == merge_like_on_home_page(contact_from_db.address)

        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_db)


def test_check_contact_info_on_home_page(app):
    home_page_contacts = app.contact.get_contact_list()
    index = randrange(len(home_page_contacts))
    contact_from_home_page = home_page_contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == merge_like_on_home_page(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == merge_like_on_home_page(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == merge_like_on_home_page(contact_from_edit_page.address)

    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub('[() -]', "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [
        contact.home_phone, contact.mobile_phone, contact.work_phone, contact.second_phone]))))


def merge_email_like_on_home_page(contact):
    return re.sub(" +", " ", "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [
        contact.email1.strip(), contact.email2.strip(), contact.email3.strip()]))))


def merge_like_on_home_page(value):
    return re.sub(" +", " ", value.strip())
