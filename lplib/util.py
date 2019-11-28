import toml
import os


def read_conf():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'store.toml'), 'r') as f:
        toml_string = f.read()

    parsed_toml = toml.loads(toml_string)
    return parsed_toml
