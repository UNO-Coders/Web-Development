from pydantic.main import BaseModel
from uuid import UUID, uuid4
from typing import List, Any
import random as r


class ApiReposnseDTO(BaseModel):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)

    id: UUID = uuid4()
    userName: str  # provide a username (mandatory field)
    phoneNumber: int = 0  # provide a phone number (optional field)[default 0]
    email: str  # provide a emal id (mandatory field)


class UserInfoRepository(object):
    def get_random_phone_number(self) -> int:
        """Function to generate random phone number

        Returns:
            int: phone number
        """
        phone_number: List[int] = []
        phone_number.append(r.randint(6, 9))
        for _ in range(1, 10):
            phone_number.append(r.randint(0, 9))
        return int("".join(map(str, phone_number)))

    def get_all_users(self, limit: int = 10) -> List[ApiReposnseDTO]:
        response: List[ApiReposnseDTO] = []
        for i in range(limit):
            response.append(
                ApiReposnseDTO(
                    userName=f"userName_{str(i+1)}",
                    phoneNumber=self.get_random_phone_number(),
                    email=f"email_{str(i+1)}@gmail.com",
                ).dict()
            )
        return response
