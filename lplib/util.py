import toml


def read_conf():
    with open('lplib/store.toml', 'r') as f:
        toml_string = f.read()

    parsed_toml = toml.loads(toml_string)
    return parsed_toml
