from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    #########
    def open_contact_fill_form(self):
        wd = self.app.wd
        if not self.is_contact_fill_page():
            wd.find_element_by_link_text("add new").click()

    def is_contact_fill_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0

    #########
    def open_home_page(self):
        wd = self.app.wd
        if not self.is_home_page():
            wd.find_element_by_link_text("home").click()
            wd.find_element_by_name("searchstring")

    def is_home_page(self):
        wd = self.app.wd
        return wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("add")) > 0

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    #########
    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    #########
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
        self.fill_field("email", contact.email1)
        self.fill_field("email2", contact.email2)
        self.fill_field("email3", contact.email3)
        self.fill_field("homepage", contact.homepage)

        self.fill_dpop_down_field("bday", contact.bday)
        self.fill_dpop_down_field("bmonth", contact.bmonth)

        self.fill_field("byear", contact.byear)

        self.fill_dpop_down_field("aday", contact.aday)
        self.fill_dpop_down_field("amonth", contact.amonth)

        self.fill_field("ayear", contact.ayear)
        self.fill_field("address2", contact.second_address)
        self.fill_field("phone2", contact.second_phone)
        self.fill_field("notes", contact.notes)

    #########
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name = 'entry']"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                id = element.find_element_by_xpath(".//input").get_attribute("id")
                self.contact_cache.append(
                    Contact(firstname=first_name, lastname=last_name, address=address, id=id,
                            all_phones_from_home_page=all_phones, all_email_from_home_page=all_email))
        return self.contact_cache

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    #########
    def create(self, contact):
        wd = self.app.wd
        self.open_contact_fill_form()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value= 'Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[text()='Record successful deleted']")
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value= 'Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[text()='Record successful deleted']")
        self.open_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_modify_by_index(index)
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_modify_by_id(id)
        self.fill_contact_form(contact)
        # submit contact edit
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_modify_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//tr[%s]/td[8]/a" % (index + 2)).click()

    def open_contact_to_modify_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//input[@id= '%s']/ancestor::tr/td[8]/a" % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//tr[%s]/td[7]/a" % (index + 2)).click()

    def add_contact_with_id_to_group_with_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_id(contact_id)
        self.select_group_from_drop_list_by_id(group_id)
        # submit contact add
        wd.find_element_by_css_selector("input[name=add]").click()
        self.open_home_page()

    def select_group_from_drop_list_by_id(self, group_id):
        wd = self.app.wd
        Select(wd.find_element_by_name("to_group")).select_by_value(group_id)

    def delete_contact_with_id_from_group_with_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        self.open_page_contacts_for_group_with_id(group_id)
        self.select_contact_by_id(contact_id)
        # submit contact delete from group
        wd.find_element_by_name("remove").click()
        self.open_home_page()

    def open_page_contacts_for_group_with_id(self, group_id):
        wd = self.app.wd
        Select(wd.find_element_by_name("group")).select_by_value(group_id)
        wd.find_element_by_name("remove")

    #########
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_modify_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")

        id = wd.find_element_by_name("id").get_attribute("value")

        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        second_phone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id, home_phone=home_phone,
                       work_phone=work_phone, mobile_phone=mobile_phone, second_phone=second_phone, email1=email1,
                       email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        second_phone = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, second_phone=second_phone)
