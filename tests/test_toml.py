import mdformat

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
