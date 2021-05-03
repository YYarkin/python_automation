# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(
        Contact(firstname="ModAutotest", middlename="ModAutotest", lastname="ModAutotestov", nickname="ModAT",
                title="Python", company="BOBRY", address="River", home_phone="8", mobile_phone="800", work_phone="535",
                fax="3535", email="BobryVsegdaDobry", homepage="google.com", bday="1", bmonth="January", byear="1991",
                aday="1", amonth="January", ayear="1991", address2="River street", phone2="house"))
    app.session.logout()
