# Stubs for cryptography.x509.general_name (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import abc
from typing import Any

class UnsupportedGeneralNameType(Exception):
    type: Any = ...
    def __init__(self, msg: Any, type: Any) -> None: ...

class GeneralName(metaclass=abc.ABCMeta):
    def value(self) -> Any: ...

class RFC822Name:
    def __init__(self, value: Any) -> None: ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

class DNSName:
    def __init__(self, value: Any) -> None: ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

class UniformResourceIdentifier:
    def __init__(self, value: Any) -> None: ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

class DirectoryName:
    def __init__(self, value: Any) -> None: ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

class RegisteredID:
    def __init__(self, value: Any) -> None: ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

class IPAddress:
    def __init__(self, value: Any) -> None: ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

class OtherName:
    def __init__(self, type_id: Any, value: Any) -> None: ...
    type_id: Any = ...
    value: Any = ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __hash__(self): ...

_GENERAL_NAMES: Any