from api.clients.public_client import PublicAPIClient
from api.models.api_response import APIResponse


class AuthClient:
    def __init__(self, client:PublicAPIClient):
        self.client = client

    def verify_login(self, email:str, password:str) -> APIResponse[dict]:
        response = self.client.post("/verifyLogin", data={"email": email, "password": password})
        return APIResponse(
            status_code=response.status_code,
            data=response.json()
        )

