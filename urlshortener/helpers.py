"""Helpers for the urlshortener"""
from random import choice
from string import ascii_letters, digits

from django.conf import settings

CONFUSING_CHARS = ["1lIo0Ogqmrn2Z"]
AVAILABLE_CHARS = ascii_letters + digits


def create_random_code(chars: str = AVAILABLE_CHARS, max_length: int = settings.MAX_URL_CHARS) -> str:
    """Create a random shortcode with predetermined length."""

    return "".join(
        [choice(chars) for _ in range(max_length)]
    )
