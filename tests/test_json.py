import mdformat

import mdformat_config


def test_format_json():
    unformatted = """{"a": 1, "b": 2}"""
    formatted = """{
    "a": 1,
    "b": 2
}
"""
    assert mdformat_config.format_json(unformatted) == formatted


def test_format_json__integration():
    unformatted_md = """```json
{"a": 1, "b": 2}
```
"""
    formatted_md = """~~~json
{
    "a": 1,
    "b": 2
}
~~~
"""
    assert mdformat.text(unformatted_md, codeformatters={"json"}) == formatted_md
