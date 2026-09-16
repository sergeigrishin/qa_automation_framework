from api.clients.api_client import APIClient
from api.models.api_response import APIResponse
from api.data.user import User
from api.schemas.users.user_response import UserResponse
from api.schemas.users.user_detail_response import UserDetailResponse
from api.schemas.users.user_request import UserRequest
import allure


class UserClient:
    """
    Клиент для работы с user
    """

    def __init__(self, client: APIClient):
        self.client = client

    def _build_user_data(self, user: User) -> dict:
        request = UserRequest(
            name=user.name,
            email=user.email,
            password=user.password,
            title=user.title,
            birth_date="10",
            birth_month="5",
            birth_year="1995",
            firstname=user.first_name,
            lastname=user.last_name,
            company="Test Company",
            address1=user.address,
            address2="",
            country="United States",
            zipcode=user.zipcode,
            state=user.state,
            city=user.city,
            mobile_number=user.mobile_number,
        )

        return request.model_dump()


    @allure.step("Создать аккаунт пользователя")
    def create_account(self, user: User) -> APIResponse[UserResponse]:
        response = self.client.post("/createAccount", data=self._build_user_data(user)
                                    )
        return self.client.parse_response(response, UserResponse)


    @allure.step("Обновить аккаунт пользователя")
    def update_account(self, user: User) -> APIResponse[UserResponse]:
        response = self.client.put("/updateAccount", data={
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
        })
        return self.client.parse_response(response, UserResponse)


    @allure.step("Проверить логин пользователя")
    def verify_login(self, email: str, password: str) -> APIResponse[UserResponse]:
        response = self.client.post("/verifyLogin", data={"email": email, "password": password})
        return self.client.parse_response(response, UserResponse)


    @allure.step("Поиск пользователя по email")
    def get_user_by_email(self, email: str) -> APIResponse[UserDetailResponse | UserResponse]:
        response = self.client.get(
            "/getUserDetailByEmail",
            params={"email": email}
        )
        data = response.json()
        if "user" in data:
            return self.client.parse_response(response, UserDetailResponse)

        return self.client.parse_response(response, UserResponse)


    @allure.step("Удалить аккаунт пользователя")
    def delete_account(self, email: str, password: str) -> APIResponse[UserResponse]:
        response = self.client.delete('/deleteAccount', data={"email": email, "password": password})

        return self.client.parse_response(response, UserResponse)
