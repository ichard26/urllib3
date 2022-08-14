try:
    import brotlicffi as brotli  # type: ignore[import]
except ImportError:
    import brotli  # type: ignore[import]

from .. import response


class BrotliDecoder(response.ContentDecoder):
    # Supports both 'brotlipy' and 'Brotli' packages
    # since they share an import name. The top branches
    # are for 'brotlipy' and bottom branches for 'Brotli'
    def __init__(self) -> None:
        self._obj = brotli.Decompressor()
        if hasattr(self._obj, "decompress"):
            setattr(self, "decompress", self._obj.decompress)
        else:
            setattr(self, "decompress", self._obj.process)

    def flush(self) -> bytes:
        if hasattr(self._obj, "flush"):
            return self._obj.flush()  # type: ignore[no-any-return]
        return b""
