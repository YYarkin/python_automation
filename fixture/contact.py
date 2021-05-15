from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_fill_form(self):
        wd = self.app.wd
        if not self.is_contact_fill_page():
            wd.find_element_by_link_text("add new").click()

    def is_contact_fill_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0

    def is_home_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def open_home_page(self):
        wd = self.app.wd
        if not self.is_home_page():
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_fill_form()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value= 'Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        # select first contact and init contact edit
        wd.find_element_by_xpath("//tr[2]/td[8]/a").click()
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def fill_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_dpop_down_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fill_field("firstname", contact.firstname)
        self.fill_field("middlename", contact.middlename)
        self.fill_field("lastname", contact.lastname)
        self.fill_field("nickname", contact.nickname)
        self.fill_field("title", contact.title)
        self.fill_field("company", contact.company)
        self.fill_field("address", contact.address)
        self.fill_field("home", contact.home_phone)
        self.fill_field("mobile", contact.mobile_phone)
        self.fill_field("work", contact.work_phone)
        self.fill_field("fax", contact.fax)
        self.fill_field("email", contact.email)
        self.fill_field("homepage", contact.homepage)

        self.fill_dpop_down_field("bday", contact.bday)
        self.fill_dpop_down_field("bmonth", contact.bmonth)

        self.fill_field("byear", contact.byear)

        self.fill_dpop_down_field("aday", contact.aday)
        self.fill_dpop_down_field("amonth", contact.amonth)

        self.fill_field("ayear", contact.ayear)
        self.fill_field("address2", contact.address2)
        self.fill_field("phone2", contact.phone2)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))
