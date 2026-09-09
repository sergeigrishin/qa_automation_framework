from httpx import Client, Response
from typing import TypeVar

from pydantic import BaseModel

from api.models.api_response import APIResponse

T = TypeVar("T", bound=BaseModel)


class APIClient:
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: str) -> Response:
        return self.client.get(url)

    def post(self, url: str, data: dict | None = None) -> Response:
        return self.client.post(url=url, data=data)

    def parse_response(self, response: Response, model: type[T]) -> APIResponse[T]:
        data = response.json()
        parsed_data = model.model_validate(data)

        return APIResponse(
            status_code=response.status_code,
            data=parsed_data
        )

    def close(self):
        self.client.close()
