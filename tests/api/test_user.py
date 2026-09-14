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
def test_registration_valid(auth_client, registered_user):
    user = User()
    response = auth_client.create_account(user)

    assert response.data['responseCode'] == HTTPStatus.CREATED


@pytest.mark.positive
@pytest.mark.api
def test_delete_account(auth_client):
    user = User()
    response = auth_client.create_account(user)
    assert response.data['responseCode'] == HTTPStatus.CREATED

    delete_response = auth_client.delete_account(
        user.email,
        user.password
    )
    assert delete_response.data['responseCode'] == HTTPStatus.OK


@pytest.mark.positive
@pytest.mark.api
def test_get_user_by_email(registered_user, auth_client):
    response = auth_client.get_user_by_email(registered_user.email)

    assert response.data['responseCode'] == HTTPStatus.OK
    assert response.data['user']['email'] == registered_user.email


@pytest.mark.positive
@pytest.mark.api
def test_update_user(registered_user, auth_client):
    print("Проверить", registered_user)
    registered_user.name = "Vasya"
    auth_client.update_account(registered_user)
    update_user = auth_client.get_user_by_email(registered_user.email)
    print("Проверить", update_user.data)
    assert update_user.data["user"]["name"] == "Vasya"