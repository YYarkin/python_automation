# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(
        Contact(firstname="Autotest", middlename="Autotest", lastname="Autotestov", nickname="AT", title="Python",
                company="BOBRY", address="River", home_phone="8", mobile_phone="800", work_phone="535", fax="3535",
                email="BobryVsegdaDobry", homepage="google.com", bday="1", bmonth="January", byear="1991", aday="1",
                amonth="January", ayear="1991", address2="River street", phone2="house"))
    app.session.logout()
