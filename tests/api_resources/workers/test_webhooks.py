# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from handinger import Handinger, AsyncHandinger
from tests.utils import assert_matches_type
from handinger.types.workers import Webhook, WebhookExecutionList

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Handinger) -> None:
        webhook = client.workers.webhooks.retrieve(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Handinger) -> None:
        response = client.workers.webhooks.with_raw_response.retrieve(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Handinger) -> None:
        with client.workers.webhooks.with_streaming_response.retrieve(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Handinger) -> None:
        webhook = client.workers.webhooks.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            url="https://example.com/handinger-webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Handinger) -> None:
        response = client.workers.webhooks.with_raw_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            url="https://example.com/handinger-webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Handinger) -> None:
        with client.workers.webhooks.with_streaming_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            url="https://example.com/handinger-webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.webhooks.with_raw_response.update(
                worker_id="",
                url="https://example.com/handinger-webhook",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Handinger) -> None:
        webhook = client.workers.webhooks.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Handinger) -> None:
        response = client.workers.webhooks.with_raw_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Handinger) -> None:
        with client.workers.webhooks.with_streaming_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_executions(self, client: Handinger) -> None:
        webhook = client.workers.webhooks.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(WebhookExecutionList, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_executions_with_all_params(self, client: Handinger) -> None:
        webhook = client.workers.webhooks.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            page=1,
        )
        assert_matches_type(WebhookExecutionList, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_executions(self, client: Handinger) -> None:
        response = client.workers.webhooks.with_raw_response.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookExecutionList, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_executions(self, client: Handinger) -> None:
        with client.workers.webhooks.with_streaming_response.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookExecutionList, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_executions(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.webhooks.with_raw_response.list_executions(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_regenerate_token(self, client: Handinger) -> None:
        webhook = client.workers.webhooks.regenerate_token(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_regenerate_token(self, client: Handinger) -> None:
        response = client.workers.webhooks.with_raw_response.regenerate_token(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_token(self, client: Handinger) -> None:
        with client.workers.webhooks.with_streaming_response.regenerate_token(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_regenerate_token(self, client: Handinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            client.workers.webhooks.with_raw_response.regenerate_token(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncHandinger) -> None:
        webhook = await async_client.workers.webhooks.retrieve(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.webhooks.with_raw_response.retrieve(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.webhooks.with_streaming_response.retrieve(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.webhooks.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHandinger) -> None:
        webhook = await async_client.workers.webhooks.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            url="https://example.com/handinger-webhook",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.webhooks.with_raw_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            url="https://example.com/handinger-webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.webhooks.with_streaming_response.update(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            url="https://example.com/handinger-webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.webhooks.with_raw_response.update(
                worker_id="",
                url="https://example.com/handinger-webhook",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHandinger) -> None:
        webhook = await async_client.workers.webhooks.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.webhooks.with_raw_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.webhooks.with_streaming_response.delete(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_executions(self, async_client: AsyncHandinger) -> None:
        webhook = await async_client.workers.webhooks.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(WebhookExecutionList, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_executions_with_all_params(self, async_client: AsyncHandinger) -> None:
        webhook = await async_client.workers.webhooks.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
            page=1,
        )
        assert_matches_type(WebhookExecutionList, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_executions(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.webhooks.with_raw_response.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookExecutionList, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_executions(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.webhooks.with_streaming_response.list_executions(
            worker_id="t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookExecutionList, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_executions(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.webhooks.with_raw_response.list_executions(
                worker_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_regenerate_token(self, async_client: AsyncHandinger) -> None:
        webhook = await async_client.workers.webhooks.regenerate_token(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_token(self, async_client: AsyncHandinger) -> None:
        response = await async_client.workers.webhooks.with_raw_response.regenerate_token(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_token(self, async_client: AsyncHandinger) -> None:
        async with async_client.workers.webhooks.with_streaming_response.regenerate_token(
            "t_org_123_w_01HZY2ZJQ8G7K42W2D7WF6V4GM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_regenerate_token(self, async_client: AsyncHandinger) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `worker_id` but received ''"):
            await async_client.workers.webhooks.with_raw_response.regenerate_token(
                "",
            )
