# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Autotest", middlename="Autotest", lastname="Autotestov", nickname="AT", title="Python",
                      company="BOBRY", address="River", home_phone="8", mobile_phone="800", work_phone="535",
                      fax="3535", email="BobryVsegdaDobry", homepage="google.com", bday="1", bmonth="January",
                      byear="1991", aday="1", amonth="January", ayear="1991", address2="River street", phone2="house")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
