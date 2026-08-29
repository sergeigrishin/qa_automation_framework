from faker import Faker
from tests.data.user_default import User

fake = Faker()


class UserFactory:

    def create_user(self):
        user = User(
            name=fake.name(),
            email=fake.email(),
            password=fake.password(length=10),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            address=fake.street_address(),
            state=fake.state(),
            city=fake.city(),
            zipcode=fake.zipcode(),
            mobile_number=fake.phone_number()
        )
        return user
