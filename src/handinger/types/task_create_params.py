# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """Worker id the task belongs to."""

    instructions: str
    """Persistent system prompt the worker uses for every task it runs."""

    output_schema: Annotated[Dict[str, object], PropertyInfo(alias="outputSchema")]
    """
    Optional JSON Schema (Draft-07) describing the structured object the worker must
    produce. When set, every task response is validated against the schema and
    exposed as `structuredOutput`.
    """

    prompt: str
    """
    Natural-language description of the worker to use for AI-generated instructions
    when `instructions` is omitted.
    """

    title: str
    """Optional display name.

    When omitted, Handinger assigns a random dog-themed name.
    """

    visibility: Literal["public", "private"]
    """`public` (default) is visible to all org members.

    `private` is only visible to invited members.
    """
