"""Helpers for the shorturl"""
from random import choice
from string import ascii_letters
from string import digits

from django.conf import settings

CONFUSING_CHARS = {c for c in '1lIo0Omn'}
AVAILABLE_CHARS = sorted(
    list({c for c in ascii_letters + digits} - CONFUSING_CHARS),
)


def create_random_code(chars: list = AVAILABLE_CHARS,
                       max_length: int = settings.MAX_URL_CHARS) -> str:
    """Create a random shortcode with predetermined length."""

    return ''.join(
        [choice(chars) for _ in range(max_length)],
    )
