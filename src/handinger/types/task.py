# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Task", "Totals"]


class Totals(BaseModel):
    credits: float

    duration_ms: float = FieldInfo(alias="durationMs")

    turn_count: float = FieldInfo(alias="turnCount")


class Task(BaseModel):
    id: str

    completed_at: Optional[str] = FieldInfo(alias="completedAt", default=None)

    created_at: str = FieldInfo(alias="createdAt")

    created_by_user_id: Optional[str] = FieldInfo(alias="createdByUserId", default=None)

    organization_id: str = FieldInfo(alias="organizationId")

    status: Literal["pending", "running", "completed", "error", "aborted"]

    title: str

    totals: Totals

    triggered_by: Literal["api", "email", "schedule", "ui"] = FieldInfo(alias="triggeredBy")

    url: str
    """Web URL of the task in the Handinger dashboard."""

    worker_id: str = FieldInfo(alias="workerId")
