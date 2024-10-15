__version__ = "0.2.0"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import io
import json
import subprocess

import ruamel.yaml

yaml = ruamel.yaml.YAML()
# Make sure to always have `sequence >= offset + 2`
yaml.indent(mapping=2, sequence=4, offset=2)


def format_json(unformatted: str, _info_str: str) -> str:
    parsed = json.loads(unformatted)
    return json.dumps(parsed, indent=2) + "\n"


def format_toml(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode()
    result = subprocess.run(
        [
            "taplo",
            "fmt",
            "--no-auto-config",
            "--colors",
            "never",
            "--option",
            "array_auto_collapse=false",
            "-",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        input=unformatted_bytes,
    )
    if result.returncode:
        raise Exception("Failed to format TOML")
    return result.stdout.decode()


def format_yaml(unformatted: str, _info_str: str) -> str:
    parsed = yaml.load(unformatted)
    dump_stream = io.StringIO()
    yaml.dump(parsed, stream=dump_stream)
    return dump_stream.getvalue()
