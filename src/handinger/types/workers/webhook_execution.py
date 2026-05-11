# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookExecution"]


class WebhookExecution(BaseModel):
    id: str

    created_at: datetime = FieldInfo(alias="createdAt")

    duration_ms: int = FieldInfo(alias="durationMs")
    """Wall-clock time spent on the delivery attempt."""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Failure reason when `requestStatus` is `error`."""

    request_status: Literal["success", "error"] = FieldInfo(alias="requestStatus")
    """`success` when the endpoint returned a 2xx response, `error` otherwise."""

    response_status: Optional[int] = FieldInfo(alias="responseStatus", default=None)
    """HTTP status returned by the endpoint, when reachable."""

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
    """Task that triggered the delivery, when available."""

    task_title: Optional[str] = FieldInfo(alias="taskTitle", default=None)
    """Title of the originating task, when available."""

    url: str
    """Endpoint Handinger attempted to deliver to."""

    worker_id: str = FieldInfo(alias="workerId")
