import pytest
from api.data.user_default import UserDefault
from http import HTTPStatus
from api.data.user import User

@pytest.mark.positive
@pytest.mark.api
def test_auth_login_with_valid_credentials(auth_client):
    user_default = UserDefault()
    response = auth_client.verify_login(email=user_default.email, password=user_default.password)

    assert response.data['responseCode'] == HTTPStatus.OK


@pytest.mark.negative
@pytest.mark.api
@pytest.mark.parametrize("email, password", [('email.ru', ''), ('test@mal.ru', "Qwerrr")])
def test_auth_login_with_invalid_credentials(auth_client, email, password):
    response = auth_client.verify_login(email=email, password=password)

    assert response.data['responseCode'] == HTTPStatus.NOT_FOUND


@pytest.mark.positive
@pytest.mark.api
def test_registration_valid(auth_client):
    user = User()
    response = auth_client.create_account(user)

    assert response.data['responseCode'] == HTTPStatus.CREATED