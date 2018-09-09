import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'secondpro.settings')

import django
django.setup()
from protwo.models import User


from faker import Faker

fakegen = Faker()

def populate(N=5):
    for user in range(N):
        fake_name = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        person = User.objects.get_or_create(name=fake_name, lastname=fake_lastname, email=fake_email)[0]




if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('Populating complete')

