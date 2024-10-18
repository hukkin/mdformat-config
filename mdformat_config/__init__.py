__version__ = "0.2.1"  # DO NOT EDIT THIS LINE MANUALLY. LET bump2version UTILITY DO IT

import io
import json
import subprocess
from pathlib import Path
import sys

import ruamel.yaml

yaml = ruamel.yaml.YAML()
# Make sure to always have `sequence >= offset + 2`
yaml.indent(mapping=2, sequence=4, offset=2)


def format_json(unformatted: str, _info_str: str) -> str:
    parsed = json.loads(unformatted)
    return json.dumps(parsed, indent=2) + "\n"


def format_toml(unformatted: str, _info_str: str) -> str:
    unformatted_bytes = unformatted.encode()
    subprocess_kwargs = {
        "stdout": subprocess.PIPE,
        "stderr": subprocess.DEVNULL,
        "input": unformatted_bytes,
    }
    taplo_args = [
        "fmt",
        "--no-auto-config",
        "--colors",
        "never",
        "--option",
        "array_auto_collapse=false",
        "-",
    ]
    try:
        result = subprocess.run(["taplo"] + taplo_args, **subprocess_kwargs)
    except FileNotFoundError:
        # taplo is not in path if the user installed with e.g.
        # `pipx install mdformat && pipx inject mdformat mdformat-config`
        # Try to look for taplo binary in the virtual environment.
        taplo_path = Path(sys.executable).parent / "taplo"
        result = subprocess.run([str(taplo_path)] + taplo_args, **subprocess_kwargs)

    if result.returncode:
        raise Exception("Failed to format TOML")
    return result.stdout.decode()


def format_yaml(unformatted: str, _info_str: str) -> str:
    parsed = yaml.load(unformatted)
    dump_stream = io.StringIO()
    yaml.dump(parsed, stream=dump_stream)
    return dump_stream.getvalue()
