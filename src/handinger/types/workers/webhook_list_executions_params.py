# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WebhookListExecutionsParams"]


class WebhookListExecutionsParams(TypedDict, total=False):
    page: int
    """Page number (1-indexed). Defaults to 1."""
