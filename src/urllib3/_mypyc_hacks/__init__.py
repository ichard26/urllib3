"""
Workarounds for mypyc.

- mypyc doesn't support nested or conditional classes so we define them here and import them as
  needed at their definition site.
  - NOTE: some classes are defined in submodules as they depend on modules that may not be
    available
"""


class BaseSSLError(BaseException):
    pass
