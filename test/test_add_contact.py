# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="Autotest", middlename="Autotest", lastname="Autotestov", nickname="AT", title="Python",
                company="BOBRY", address="River", home_phone="8", mobile_phone="800", work_phone="535", fax="3535",
                email="BobryVsegdaDobry", homepage="google.com", bday="1", bmonth="January", byear="1991", aday="1",
                amonth="January", ayear="1991", address2="River street", phone2="house"))