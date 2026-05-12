# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScheduleCreateParams", "When", "WhenScheduledWhen", "WhenDelayedWhen", "WhenCronWhen", "WhenIntervalWhen"]


class ScheduleCreateParams(TypedDict, total=False):
    input: Required[str]

    when: Required[When]

    budget: Literal["low", "standard", "high", "unlimited"]


class WhenScheduledWhen(TypedDict, total=False):
    date: Required[str]

    type: Required[Literal["scheduled"]]


class WhenDelayedWhen(TypedDict, total=False):
    delay_in_seconds: Required[Annotated[int, PropertyInfo(alias="delayInSeconds")]]

    type: Required[Literal["delayed"]]


class WhenCronWhen(TypedDict, total=False):
    cron: Required[str]

    type: Required[Literal["cron"]]


class WhenIntervalWhen(TypedDict, total=False):
    interval_seconds: Required[Annotated[int, PropertyInfo(alias="intervalSeconds")]]

    type: Required[Literal["interval"]]


When: TypeAlias = Union[WhenScheduledWhen, WhenDelayedWhen, WhenCronWhen, WhenIntervalWhen]
