from typing import Any
# Copyright (c) 2016 Google Inc. (under http://www.apache.org/licenses/LICENSE-2.0)
def decoration(func):
    # type: (Any) -> Any
    return func

@decoration
def f1(a):
    # type: (Any) -> None
    pass
