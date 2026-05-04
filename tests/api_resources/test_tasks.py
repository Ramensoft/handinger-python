# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from handinger import Handinger, AsyncHandinger
from tests.utils import assert_matches_type
from handinger.types import Worker, TaskWithTurns

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Handinger) -> None:
        task = client.tasks.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Handinger) -> None:
        task = client.tasks.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            instructions="instructions",
            visibility="public",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Handinger) -> None:
        response = client.tasks.with_raw_response.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Handinger) -> None:
        with client.tasks.with_streaming_response.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(Worker, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Handinger) -> None:
        task = client.tasks.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Handinger) -> None:
        response = client.tasks.with_raw_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Handinger) -> None:
        with client.tasks.with_streaming_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskWithTurns, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            client.tasks.with_raw_response.retrieve(
                "",
            )


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            instructions="instructions",
            visibility="public",
        )
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHandinger) -> None:
        response = await async_client.tasks.with_raw_response.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(Worker, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHandinger) -> None:
        async with async_client.tasks.with_streaming_response.create(
            title="Brand voice analyzer",
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(Worker, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHandinger) -> None:
        task = await async_client.tasks.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHandinger) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskWithTurns, task, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHandinger) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            "tsk_01HZY31W2SZJ8MJ2FQTR3M1K9D",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskWithTurns, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_id` but received ''"):
            await async_client.tasks.with_raw_response.retrieve(
                "",
            )
