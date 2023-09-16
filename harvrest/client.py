"""Clinet interface for harvrest.

Decribes base url, headers, and methods for making requests to a web API.
"""

from typing import Protocol


class AuthenticationProtocol(Protocol):
    """Interface for authentication."""

    def authenticate(self) -> None:
        """Authenticate with a web API."""


class Client(Protocol):
    """Interface for a client."""

    base_url: str
    headers: dict[str, str]

    def get(self, url: str) -> dict:
        """Make a get request to a web API."""
