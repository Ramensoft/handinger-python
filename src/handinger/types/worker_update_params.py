# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkerUpdateParams"]


class WorkerUpdateParams(TypedDict, total=False):
    instructions: str
    """Replaces the persistent system prompt.

    Subsequent tasks pick up the new instructions immediately; in-flight tasks keep
    using the previous version.
    """

    output_schema: Annotated[Optional[Dict[str, object]], PropertyInfo(alias="outputSchema")]
    """Replace the worker's structured output schema.

    Pass `null` to clear it and return to free-form text responses.
    """

    summary: str
    """Replaces the worker's short one-line summary."""

    title: str
    """New display name for the worker."""

    visibility: Literal["public", "private"]
    """
    Change visibility between `public` (any org member can run tasks) and `private`
    (only invited members).
    """
