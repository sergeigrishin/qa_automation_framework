from http import HTTPStatus

import pytest

from api.data.user import User
from api.data.user_default import UserDefault


@pytest.mark.positive
@pytest.mark.api
@pytest.mark.flaky(reruns=1)
def test_auth_login_with_valid_credentials(user_client):
    user_default = UserDefault()
    response = user_client.verify_login(email=user_default.email, password=user_default.password)

    assert response.data.response_code == HTTPStatus.OK


@pytest.mark.negative
@pytest.mark.api
@pytest.mark.parametrize("email, password", [('email.ru', ''), ('test@mal.ru', "Qwerrr")])
def test_auth_login_with_invalid_credentials(user_client, email, password):
    response = user_client.verify_login(email=email, password=password)

    assert response.data.response_code == HTTPStatus.NOT_FOUND


@pytest.mark.positive
@pytest.mark.api
def test_registration_valid(user_client):
    user = User()
    response = user_client.create_account(user)

    assert response.data.response_code == HTTPStatus.CREATED

    user_client.delete_account(
        email=user.email,
        password=user.password
    )


@pytest.mark.positive
@pytest.mark.api
def test_delete_account(user_client):
    user = User()
    response = user_client.create_account(user)

    assert response.data.response_code == HTTPStatus.CREATED

    delete_response = user_client.delete_account(
        user.email,
        user.password
    )

    assert delete_response.data.response_code == HTTPStatus.OK


@pytest.mark.positive
@pytest.mark.api
def test_get_user_by_email(registered_user, user_client):
    response = user_client.get_user_by_email(registered_user.email)

    assert response.data.response_code == HTTPStatus.OK
    assert response.data.user.email == registered_user.email
    assert response.data.user.name == registered_user.name


@pytest.mark.negative
@pytest.mark.api
def test_get_user_by_invalid_email(user_client):
    response = user_client.get_user_by_email('not_email_nvbvn@mail.com')
    assert response.data.response_code == HTTPStatus.NOT_FOUND


@pytest.mark.positive
@pytest.mark.api
def test_update_user(registered_user, user_client):
    registered_user.name = "Mark"

    response = user_client.update_account(registered_user)
    assert response.data.response_code == HTTPStatus.OK

    update_user = user_client.get_user_by_email(registered_user.email)

    assert update_user.data.user.name == "Mark"


@pytest.mark.negative
@pytest.mark.api
def test_update_user_invalid_password(user_client, registered_user):
    registered_user.password = 'invalidpassword'
    registered_user.name = 'Mark'

    response = user_client.update_account(registered_user)

    assert response.data.response_code == HTTPStatus.NOT_FOUND
