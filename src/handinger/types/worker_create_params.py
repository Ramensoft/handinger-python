# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["WorkerCreateParams"]


class WorkerCreateParams(TypedDict, total=False):
    instructions: str
    """Persistent system prompt the worker uses for every task it runs."""

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
