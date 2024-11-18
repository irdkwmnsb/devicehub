from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.default_response import DefaultResponse
from ...models.devices_payload import DevicesPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DevicesPayload,
    present: Union[Unset, bool] = UNSET,
    booked: Union[Unset, bool] = UNSET,
    annotated: Union[Unset, bool] = UNSET,
    controlled: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["present"] = present

    params["booked"] = booked

    params["annotated"] = annotated

    params["controlled"] = controlled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": "/devices",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DefaultResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DefaultResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DefaultResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: DevicesPayload,
    present: Union[Unset, bool] = UNSET,
    booked: Union[Unset, bool] = UNSET,
    annotated: Union[Unset, bool] = UNSET,
    controlled: Union[Unset, bool] = UNSET,
) -> Response[DefaultResponse]:
    """Removes devices

     Removes devices from the database

    Args:
        present (Union[Unset, bool]):
        booked (Union[Unset, bool]):
        annotated (Union[Unset, bool]):
        controlled (Union[Unset, bool]):
        body (DevicesPayload): Payload object for adding/removing devices

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DefaultResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        present=present,
        booked=booked,
        annotated=annotated,
        controlled=controlled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: DevicesPayload,
    present: Union[Unset, bool] = UNSET,
    booked: Union[Unset, bool] = UNSET,
    annotated: Union[Unset, bool] = UNSET,
    controlled: Union[Unset, bool] = UNSET,
) -> Optional[DefaultResponse]:
    """Removes devices

     Removes devices from the database

    Args:
        present (Union[Unset, bool]):
        booked (Union[Unset, bool]):
        annotated (Union[Unset, bool]):
        controlled (Union[Unset, bool]):
        body (DevicesPayload): Payload object for adding/removing devices

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DefaultResponse
    """

    return sync_detailed(
        client=client,
        body=body,
        present=present,
        booked=booked,
        annotated=annotated,
        controlled=controlled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DevicesPayload,
    present: Union[Unset, bool] = UNSET,
    booked: Union[Unset, bool] = UNSET,
    annotated: Union[Unset, bool] = UNSET,
    controlled: Union[Unset, bool] = UNSET,
) -> Response[DefaultResponse]:
    """Removes devices

     Removes devices from the database

    Args:
        present (Union[Unset, bool]):
        booked (Union[Unset, bool]):
        annotated (Union[Unset, bool]):
        controlled (Union[Unset, bool]):
        body (DevicesPayload): Payload object for adding/removing devices

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DefaultResponse]
    """

    kwargs = _get_kwargs(
        body=body,
        present=present,
        booked=booked,
        annotated=annotated,
        controlled=controlled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: DevicesPayload,
    present: Union[Unset, bool] = UNSET,
    booked: Union[Unset, bool] = UNSET,
    annotated: Union[Unset, bool] = UNSET,
    controlled: Union[Unset, bool] = UNSET,
) -> Optional[DefaultResponse]:
    """Removes devices

     Removes devices from the database

    Args:
        present (Union[Unset, bool]):
        booked (Union[Unset, bool]):
        annotated (Union[Unset, bool]):
        controlled (Union[Unset, bool]):
        body (DevicesPayload): Payload object for adding/removing devices

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DefaultResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            present=present,
            booked=booked,
            annotated=annotated,
            controlled=controlled,
        )
    ).parsed
