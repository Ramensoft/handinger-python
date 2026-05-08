# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import task_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.worker import Worker
from ..types.task_with_turns import TaskWithTurns

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    """Run and inspect tasks against a worker."""

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ramensoft/handinger-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ramensoft/handinger-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        worker_id: str,
        instructions: str | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        prompt: str | Omit = omit,
        summary: str | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """Run a new task against an existing worker.

        Send `multipart/form-data` to attach
        files; the bytes are bootstrapped into the worker's workspace before the task
        starts.

        Args:
          worker_id: Worker id the task belongs to.

          instructions: Persistent system prompt the worker uses for every task it runs.

          output_schema: Optional JSON Schema (Draft-07) describing the structured object the worker must
              produce. When set, every task response is validated against the schema and
              exposed as `structuredOutput`.

          prompt: Natural-language description of the worker to use for AI-generated instructions
              when `instructions` is omitted.

          summary: Short one-line description of the worker's purpose. Auto-generated when omitted
              and a `prompt` is provided.

          title: Optional display name. When omitted, Handinger assigns a random dog-themed name.

          visibility: `public` (default) is visible to all org members. `private` is only visible to
              invited members.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/tasks",
            body=maybe_transform(
                {
                    "worker_id": worker_id,
                    "instructions": instructions,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "summary": summary,
                    "title": title,
                    "visibility": visibility,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskWithTurns:
        """
        Retrieve a single task and its individual turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return self._get(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskWithTurns,
        )


class AsyncTasksResource(AsyncAPIResource):
    """Run and inspect tasks against a worker."""

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Ramensoft/handinger-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Ramensoft/handinger-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        worker_id: str,
        instructions: str | Omit = omit,
        output_schema: Dict[str, object] | Omit = omit,
        prompt: str | Omit = omit,
        summary: str | Omit = omit,
        title: str | Omit = omit,
        visibility: Literal["public", "private"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Worker:
        """Run a new task against an existing worker.

        Send `multipart/form-data` to attach
        files; the bytes are bootstrapped into the worker's workspace before the task
        starts.

        Args:
          worker_id: Worker id the task belongs to.

          instructions: Persistent system prompt the worker uses for every task it runs.

          output_schema: Optional JSON Schema (Draft-07) describing the structured object the worker must
              produce. When set, every task response is validated against the schema and
              exposed as `structuredOutput`.

          prompt: Natural-language description of the worker to use for AI-generated instructions
              when `instructions` is omitted.

          summary: Short one-line description of the worker's purpose. Auto-generated when omitted
              and a `prompt` is provided.

          title: Optional display name. When omitted, Handinger assigns a random dog-themed name.

          visibility: `public` (default) is visible to all org members. `private` is only visible to
              invited members.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/tasks",
            body=await async_maybe_transform(
                {
                    "worker_id": worker_id,
                    "instructions": instructions,
                    "output_schema": output_schema,
                    "prompt": prompt,
                    "summary": summary,
                    "title": title,
                    "visibility": visibility,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Worker,
        )

    async def retrieve(
        self,
        task_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskWithTurns:
        """
        Retrieve a single task and its individual turns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_id:
            raise ValueError(f"Expected a non-empty value for `task_id` but received {task_id!r}")
        return await self._get(
            path_template("/api/tasks/{task_id}", task_id=task_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskWithTurns,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
