from fixture.orm import ORMfixture
from model.contact import Contact
from model.group import Group
import random

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_random_contact_in_random_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="testov"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    add_random_contact_in_group(app=app, group=group)


def test_delete_random_contact_from_random_group(app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="testov"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contacts_in_group(group)) == 0:
        add_random_contact_in_group(app=app, group=group)
    delete_random_contact_from_group(app=app, group=group)


def add_random_contact_in_group(app, group):
    if len(db.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="test", lastname="testov"))
    contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_with_id_to_group_with_id(contact.id, group.id)
    assert (contact in db.get_contacts_in_group(group))


def delete_random_contact_from_group(app, group):
    contacts = db.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.delete_contact_with_id_from_group_with_id(contact.id, group.id)
    assert (contact not in db.get_contacts_in_group(group))
