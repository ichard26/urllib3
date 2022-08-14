import zstandard as zstd

from .. import response
from ..exceptions import DecodeError


class ZstdDecoder(response.ContentDecoder):
    def __init__(self) -> None:
        self._obj = zstd.ZstdDecompressor().decompressobj()

    def decompress(self, data: bytes) -> bytes:
        if not data:
            return b""
        return self._obj.decompress(data)  # type: ignore[no-any-return]

    def flush(self) -> bytes:
        ret = self._obj.flush()
        if not self._obj.eof:
            raise DecodeError("Zstandard data is incomplete")
        return ret  # type: ignore[no-any-return]
