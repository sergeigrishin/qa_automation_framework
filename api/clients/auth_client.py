from api.clients.public_client import PublicAPIClient
from api.models.api_response import APIResponse
from api.data.user import User


class AuthClient:
    def __init__(self, client: PublicAPIClient):
        self.client = client

    def create_account(self, user: User) -> APIResponse[dict]:
        response = self.client.post("/createAccount", data={
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "title": user.title,
            "birth_date": "10",
            "birth_month": "5",
            "birth_year": "1995",
            "firstname": user.first_name,
            "lastname": user.last_name,
            "company": "Test Company",
            "address1": user.address,
            "address2": "",
            "country": "United States",
            "zipcode": user.zipcode,
            "state": user.state,
            "city": user.city,
            "mobile_number": user.mobile_number
        }
                                    )

        return APIResponse(
            status_code=response.status_code,
            data=response.json()
        )

    def verify_login(self, email: str, password: str) -> APIResponse[dict]:
        response = self.client.post("/verifyLogin", data={"email": email, "password": password})
        return APIResponse(
            status_code=response.status_code,
            data=response.json()
        )
