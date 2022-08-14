"""
Workarounds for mypyc.

- mypyc doesn't support nested or conditional classes so we define them in this package and
  import them as needed at their definition site.
"""
