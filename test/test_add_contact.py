# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Autotest", middlename="Autotest", lastname="Autotestov", nickname="AT", title="Python",
                      company="BOBRY", address="River", home_phone="12345", mobile_phone="88005353535",
                      work_phone="09876", fax="3535", email1="Bobry", email2="Vsegda", email3="Dobry",
                      homepage="google.com", bday="1", bmonth="January", byear="1991", aday="1", amonth="January",
                      ayear="1991", second_address="River street", second_phone="5353535", notes="Hello")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
