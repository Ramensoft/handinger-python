# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .webhook_execution import WebhookExecution

__all__ = ["WebhookExecutionList"]


class WebhookExecutionList(BaseModel):
    logs: List[WebhookExecution]

    page: int
    """Current page number."""

    page_count: int = FieldInfo(alias="pageCount")
    """Total number of pages available."""

    total_count: int = FieldInfo(alias="totalCount")
    """Total number of executions recorded."""
