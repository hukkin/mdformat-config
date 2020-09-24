import mdformat_config

import mdformat


UNFORMATTED_YAML = """# Comment here
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: e1668fe86af3810fbca72b8653fe478e66a0afdc  # frozen: v3.2.0
    hooks:
      - id: check-yaml
      - id: check-toml
"""

FORMATTED_YAML = """# Comment here
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: e1668fe86af3810fbca72b8653fe478e66a0afdc    # frozen: v3.2.0
  hooks:
  - id: check-yaml
  - id: check-toml
"""


def test_format_yaml():
    assert mdformat_config.format_yaml(UNFORMATTED_YAML, "") == FORMATTED_YAML


def test_format_yaml__integration():
    unformatted_md = f"~~~yaml\n{UNFORMATTED_YAML}~~~\n"
    formatted_md = f"```yaml\n{FORMATTED_YAML}```\n"
    assert mdformat.text(unformatted_md, codeformatters={"yaml"}) == formatted_md
