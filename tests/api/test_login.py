import pytest
from tests.data.user_default import UserDefault


@pytest.mark.positive
@pytest.mark.api
def test_auth_login_with_valid_credentials(auth_client):
    user_default = UserDefault()
    response = auth_client.verify_login(email=user_default.email, password=user_default.password)

    assert response.data['responseCode'] == 200


@pytest.mark.negative
@pytest.mark.api
@pytest.mark.parametrize("email, password", [('email.ru', ''), ('test@mal.ru', "Qwerrr")])
def test_auth_login_with_invalid_credentials(auth_client, email, password):
    response = auth_client.verify_login(email=email, password=password)

    assert response.data['responseCode'] == 404
