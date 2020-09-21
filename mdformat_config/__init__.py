import json

import toml


__version__ = "0.1.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT


def format_json(unformatted: str) -> str:
    parsed = json.loads(unformatted)
    return json.dumps(parsed, indent=4) + "\n"


def format_toml(unformatted: str) -> str:
    parsed = toml.loads(unformatted, decoder=toml.TomlPreserveCommentDecoder())
    return toml.dumps(parsed, encoder=toml.TomlPreserveCommentEncoder())
