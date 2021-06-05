# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_contact_first_and_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="testov"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="ModAutotest", lastname="ModAutotestov")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(Contact.clean, new_contacts), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                         key=Contact.id_or_max)
