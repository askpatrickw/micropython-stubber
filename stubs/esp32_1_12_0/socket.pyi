
from typing import Any, Dict, Optional, Sequence, Tuple, Union
Node = Any
def getaddrinfo() -> None: ...
class socket:
    def accept() -> None: ...
    def bind() -> None: ...
    def close() -> None: ...
    def connect() -> None: ...
    def fileno() -> None: ...
    def listen() -> None: ...
    def makefile() -> None: ...
    def read() -> None: ...
    def readinto() -> None: ...
    def readline() -> None: ...
    def recv() -> None: ...
    def recvfrom() -> None: ...
    def send() -> None: ...
    def sendall() -> None: ...
    def sendto() -> None: ...
    def setblocking() -> None: ...
    def setsockopt() -> None: ...
    def settimeout() -> None: ...
    def write() -> None: ...