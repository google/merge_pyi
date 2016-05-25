# Copyright (c) 2016 Google Inc. (under http://www.apache.org/licenses/LICENSE-2.0)
from typing import Any
class C(object):
    def f(self, x):
        # type: (Any) -> None
        pass

    def g(self):
        # type: () -> Any
        def f(x): #gets ignored by pytype but fixer sees it, generates warning (FIXME?)
            # type: (Any) -> Any
            return 1
        return f
