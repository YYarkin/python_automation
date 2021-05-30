from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number_as_str(maxlen, prefix=""):
    return str(prefix) + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=random_string("fname", 5), middlename=random_string("mname", 5),
            lastname=random_string("lname", 5), nickname=random_string("AT", 5), title=random_string("Python", 5),
            company=random_string("BOBRY", 5), address=random_string("River", 5), home_phone=random_number_as_str(9),
            mobile_phone=random_number_as_str(9, "8800"), work_phone=random_number_as_str(9),
            fax=random_number_as_str(9), email1=random_string("Bobry", 5), email2=random_string("Vsegda", 5),
            email3=random_string("Dobry", 5), homepage=random_string("google", 5), bday="1", bmonth="January",
            byear="1991", aday="1", amonth="January", ayear="1991", second_address=random_string("Street", 5),
            second_phone=random_number_as_str(9), notes=random_string("Hello", 5))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
