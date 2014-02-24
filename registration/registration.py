from argparse import ArgumentParser
from copy import copy
import csv
import os.path
import sys


from constants import NO_PYTHON, NO_SQL
NO_PYTHON = copy(NO_PYTHON)
NO_SQL = copy(NO_SQL)


MY_DIR_PATH = os.path.dirname(__file__)


class Registration(object):
    def __init__(self, csv_row):
        self.__first_name = csv_row[0].strip()
        if len(self.__first_name) == 0:
            raise ValueError
        self.__last_name = csv_row[1].strip()
        if len(self.__last_name) == 0:
            raise ValueError
        self.__email = csv_row[2].strip().lower()
        if len(self.__email) == 0:
            raise ValueError
        elif not '@' in self.__email:
            raise ValueError(self.__email)
        if self.__email in NO_PYTHON:
            NO_PYTHON.remove(self.__email)
            self.__python = False
        else:
            self.__python = True
        if self.__email in NO_SQL:
            NO_SQL.remove(self.__email)
            self.__sql = False
        else:
            self.__sql = True
        if len(csv_row) > 3:
            self.__major = csv_row[3].strip()
        else:
            self.__major = None
        if len(csv_row) > 4:
            self.__laptop = csv_row[4].strip().lower() == "yes"
        else:
            self.__laptop = None

    def __eq__(self, other):
        return self.__email == other.__email

    def __cmp__(self, other):
        return cmp(self.last_name.lower(), other.last_name.lower())

    @property
    def email(self):
        return self.__email

    @property
    def first_name(self):
        return self.__first_name

    @property
    def laptop(self):
        return self.__laptop

    @property
    def last_name(self):
        return self.__last_name

    @property
    def major(self):
        return self.__major

    @property
    def python(self):
        return self.__python

    @property
    def sql(self):
        return self.__sql

    def __repr__(self):
        return "%s %s <%s>" % (self.first_name, self.last_name, self.email)


def read_registrations(file_base_name):
    registrations = []
    with open(file_base_name + '.csv') as f:
        for csv_row_i, csv_row in enumerate(csv.reader(f)):
            if csv_row_i == 0:
                continue
            if len(csv_row) == 0:
                continue
            if len(csv_row[2].strip()) == 0:
                continue
            registrations.append(Registration(csv_row))
    return registrations


python_registrations = read_registrations('python')
thursday_python_registrations = read_registrations('python_thursday')
friday_python_registrations = read_registrations('python_friday')
assert len(python_registrations) == len(thursday_python_registrations) + len(friday_python_registrations)
for python_registrations_ in (python_registrations, thursday_python_registrations, friday_python_registrations):
    for python_registration in python_registrations_:
        assert python_registration.python, python_registration
for day_python_registrations in (thursday_python_registrations, friday_python_registrations):
    for day_python_registration in day_python_registrations:
        if not day_python_registration in python_registrations:
            # print >>sys.stderr, day_python_registration, 'is registered for a day but is not in the total list'
            pass

sql_registrations = read_registrations('sql')
for sql_registration in sql_registrations:
    assert sql_registration.sql, sql_registration
assert len(NO_PYTHON) == 0, NO_PYTHON
assert len(NO_SQL) == 0, NO_SQL



argument_parser = ArgumentParser()
argument_parser.add_argument("--emails", action='store_true')
argument_parser.add_argument("--day", type=str, default='thursday')
argument_parser.add_argument("--registrations-by-major", action='store_true')
args = argument_parser.parse_args()

if args.emails:
    registrations = locals()[args.day + '_python_registrations']
    print "\n".join(str(registration) for registration in registrations)
    # print len(registrations)
elif args.registrations_by_major:
    def get_registrations_by_major(registrations):
        registrations_by_major = {}
        for registration in registrations:
            assert registration.major is not None
            registrations_by_major.setdefault(registration.major, []).append(registration)
        return registrations_by_major
    #for major, python_registrations_ in sorted(get_registrations_by_major(python_registrations).iteritems()):
    #    print major, len(python_registrations_)
