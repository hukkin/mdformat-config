import subprocess
from unittest.mock import patch
import os

import mdformat
import pytest

import mdformat_config


def test_format_toml__comments():
    unformatted = """[[products]]
name = "Nail"
sku = 284758393
# This is a comment
color = "gray" # Hello World
# name = { first = 'Tom', last = 'Preston-Werner' }
# arr7 = [
#  1, 2, 3
# ]
# lines  = '''
# The first newline is
# trimmed in raw strings.
#   All other whitespace
#   is preserved.
# '''
[animals]
color = "gray" # col
fruits = "apple" # a = [1,2,3]
a = 3
b-comment = "a is 3"
"""
    formatted = """[[products]]
name = "Nail"
sku = 284758393
# This is a comment
color = "gray" # Hello World
# name = { first = 'Tom', last = 'Preston-Werner' }
# arr7 = [
#  1, 2, 3
# ]
# lines  = '''
# The first newline is
# trimmed in raw strings.
#   All other whitespace
#   is preserved.
# '''
[animals]
color = "gray"       # col
fruits = "apple"     # a = [1,2,3]
a = 3
b-comment = "a is 3"
"""
    assert mdformat_config.format_toml(unformatted, "") == formatted


def test_format_toml__integration():
    unformatted_md = """~~~toml
[animals]
color =   "white"
[cars]
color      = "blue"
~~~
"""
    formatted_md = """```toml
[animals]
color = "white"
[cars]
color = "blue"
```
"""
    assert mdformat.text(unformatted_md, codeformatters={"toml"}) == formatted_md


@pytest.mark.skipif(
    os.name == "nt",
    reason="I don't have access to a Windows machine",
)
def test_taplo_not_in_path():
    """Test taplo binary discovery fallback if taplo not in $PATH."""
    input_ = """\
~~~toml
      [         find-taplo]
~~~
"""
    expected_output = """\
```toml
[find-taplo]
```
"""

    unmocked_run = subprocess.run

    def no_taplo_run(*args, **kwargs):
        """Make subprocess.run think that `taplo` is not in $PATH."""
        if args[0][0] == "taplo":
            raise FileNotFoundError
        return unmocked_run(*args, **kwargs)

    with patch("mdformat_config.subprocess.run", new=no_taplo_run):
        output = mdformat.text(input_, codeformatters={"toml"})
    assert output == expected_output
