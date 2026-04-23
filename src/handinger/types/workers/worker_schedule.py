# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "WorkerSchedule",
    "ScheduledWorkerSchedule",
    "DelayedWorkerSchedule",
    "CronWorkerSchedule",
    "IntervalWorkerSchedule",
]


class ScheduledWorkerSchedule(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    input: str

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["scheduled"]


class DelayedWorkerSchedule(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    delay_in_seconds: int = FieldInfo(alias="delayInSeconds")

    input: str

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["delayed"]


class CronWorkerSchedule(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    cron: str

    input: str

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["cron"]


class IntervalWorkerSchedule(BaseModel):
    id: str

    budget: Literal["low", "standard", "high", "unlimited"]

    input: str

    interval_seconds: int = FieldInfo(alias="intervalSeconds")

    next_run_at: datetime = FieldInfo(alias="nextRunAt")

    type: Literal["interval"]


WorkerSchedule: TypeAlias = Annotated[
    Union[ScheduledWorkerSchedule, DelayedWorkerSchedule, CronWorkerSchedule, IntervalWorkerSchedule],
    PropertyInfo(discriminator="type"),
]
