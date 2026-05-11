# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    url: Required[Optional[str]]
    """HTTPS endpoint Handinger should POST to when a task finishes.

    Pass `null` to remove the webhook and clear its token.
    """
