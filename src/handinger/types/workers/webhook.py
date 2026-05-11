# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    token: Optional[str] = None
    """Shared secret sent in the `X-Handinger-Token` header on each delivery.

    `null` when no webhook is configured.
    """

    url: Optional[str] = None
    """HTTPS endpoint that receives webhook deliveries when a task completes.

    `null` when no webhook is configured.
    """
