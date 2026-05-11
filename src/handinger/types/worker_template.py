# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkerTemplate"]


class WorkerTemplate(BaseModel):
    id: str

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    instructions: str

    organization_id: str = FieldInfo(alias="organizationId")

    output_schema: Optional[Dict[str, object]] = FieldInfo(alias="outputSchema", default=None)

    summary: str

    title: str

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: str = FieldInfo(alias="userId")

    visibility: Literal["public", "private"]
