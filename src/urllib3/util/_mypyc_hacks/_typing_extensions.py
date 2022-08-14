from typing import Tuple

from typing_extensions import TypedDict


class _TYPE_PEER_CERT_RET_DICT(TypedDict, total=False):
    subjectAltName: Tuple[Tuple[str, str], ...]
    subject: Tuple[Tuple[Tuple[str, str], ...], ...]
    serialNumber: str
