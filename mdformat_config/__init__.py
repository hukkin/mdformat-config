__version__ = "0.1.3"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import io
import json

import ruamel.yaml
import toml


def format_json(unformatted: str, _info_str: str) -> str:
    parsed = json.loads(unformatted)
    return json.dumps(parsed, indent=2) + "\n"


def format_toml(unformatted: str, _info_str: str) -> str:
    parsed = toml.loads(unformatted, decoder=toml.TomlPreserveCommentDecoder())
    return toml.dumps(parsed, encoder=toml.TomlPreserveCommentEncoder())


def format_yaml(unformatted: str, _info_str: str) -> str:
    yaml = ruamel.yaml.YAML()
    # Make sure to always have `sequence >= offset + 2`
    yaml.indent(mapping=2, sequence=4, offset=2)

    parsed = yaml.load(unformatted)
    dump_stream = io.StringIO()
    yaml.dump(parsed, stream=dump_stream)
    return dump_stream.getvalue()
