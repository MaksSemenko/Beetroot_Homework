import re

regex = r"^[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*[@]\w+[.]\w{3,}$"

class EMail:

    def __init__(self, email):
        self.email = email
        if not self.validate:
            self.email = f'Invalid Email: "{email}"'

    @property
    def validate(self):
        if re.search(regex, self.email):
            return True
        return False


a = EMail("abc.def@ukr.net")
b = EMail("abc..@ukr.net")
c = EMail("abc_def@ukr.net")
d = EMail("abc_def@ukr.ne")

print(a.email)
print(b.email)
print(c.email)
print(d.email)
