# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TaskCreateParams"]


class TaskCreateParams(TypedDict, total=False):
    title: Required[str]

    worker_id: Required[Annotated[str, PropertyInfo(alias="workerId")]]
    """Worker id the task belongs to."""

    instructions: str
    """Persistent system prompt the worker uses for every task it runs."""

    prompt: str
    """
    Natural-language description of the worker to use for AI-generated instructions
    when `instructions` is omitted.
    """

    visibility: Literal["public", "private"]
    """`public` (default) is visible to all org members.

    `private` is only visible to invited members.
    """
