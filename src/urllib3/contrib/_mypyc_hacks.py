"""
Workarounds for mypyc.

- mypyc doesn't support nested or conditional classes so we define them here and import them as
  needed at their definition site.
"""

from typing import Optional, TypedDict


class UnsupportedExtension(Exception):
    pass


class _TYPE_SOCKS_OPTIONS(TypedDict):
    socks_version: int
    proxy_host: Optional[str]
    proxy_port: Optional[str]
    username: Optional[str]
    password: Optional[str]
    rdns: bool
