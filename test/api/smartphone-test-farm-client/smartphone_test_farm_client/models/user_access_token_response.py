from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.token import Token


T = TypeVar("T", bound="UserAccessTokenResponse")


@_attrs_define
class UserAccessTokenResponse:
    """
    Attributes:
        success (bool):
        description (str):
        token (Token):
    """

    success: bool
    description: str
    token: "Token"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        description = self.description

        token = self.token.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "description": description,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.token import Token

        d = src_dict.copy()
        success = d.pop("success")

        description = d.pop("description")

        token = Token.from_dict(d.pop("token"))

        user_access_token_response = cls(
            success=success,
            description=description,
            token=token,
        )

        user_access_token_response.additional_properties = d
        return user_access_token_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
