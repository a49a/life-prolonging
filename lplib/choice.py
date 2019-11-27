from random import choice
import toml


class Choice:

    def __init__(self):
        self.conf = self.read_conf()

    @staticmethod
    def read_conf():
        with open('lplib/store.toml', 'r') as f:
            toml_string = f.read()

        parsed_toml = toml.loads(toml_string)
        return parsed_toml

    def choose(self, name):
        r = choice(self.conf[name])
        return r



