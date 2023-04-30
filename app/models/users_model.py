from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from bson import ObjectId
import utils


class UsersModel(BaseModel):
    user_id: utils.PyObjectId = Field(
        default_factory=utils.PyObjectId, alias="_id")
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    class Config():
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fullname": "Salman Rizqi Fatih",
                "email": "frnamlas@gmail.com",
            }
        }
