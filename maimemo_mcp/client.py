import json
import os
import sys
import httpx
from pathlib import Path
from typing import Any

_client: "MaimemoClient | None" = None


def _load_token_from_opencode_config() -> str:
    config_paths = [
        Path(os.environ.get("OPENDODE_CONFIG_PATH", "")) if os.environ.get("OPENDODE_CONFIG_PATH") else None,
        Path.home() / ".config" / "opencode" / "opencode.jsonc",
        Path.home() / ".config" / "opencode" / "opencode.json",
    ]
    for config_path in config_paths:
        if config_path and config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
                token = config.get("mcp", {}).get("maimemo", {}).get("env", {}).get("MAIMEMO_API_TOKEN", "")
                if token:
                    return token
            except Exception:
                continue
    return ""


def get_client() -> "MaimemoClient":
    global _client
    if _client is None:
        token = os.environ.get("MAIMEMO_API_TOKEN", "") or _load_token_from_opencode_config()
        if not token:
            raise RuntimeError(
                "MAIMEMO_API_TOKEN environment variable is required.\n"
                "Set it in MCP config: {\"env\": {\"MAIMEMO_API_TOKEN\": \"your-token\"}}"
            )
        _client = MaimemoClient(token)
    return _client


class MaimemoClient:
    def __init__(self, token: str):
        self._token = token
        self._base_url = os.environ.get(
            "MAIMEMO_BASE_URL", "https://open.maimemo.com/open"
        ).rstrip("/")

    @property
    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self._token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    async def get(self, path: str, params: dict | None = None) -> Any:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(
                f"{self._base_url}{path}",
                headers=self._headers,
                params=params,
            )
            response.raise_for_status()
            return response.json()

    async def post(self, path: str, json: dict | None = None) -> Any:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{self._base_url}{path}",
                headers=self._headers,
                json=json,
            )
            response.raise_for_status()
            return response.json()

    async def delete(self, path: str) -> Any:
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.delete(
                f"{self._base_url}{path}",
                headers=self._headers,
            )
            response.raise_for_status()
            if response.status_code == 204:
                return {"success": True}
            return response.json() if response.content else {"success": True}
